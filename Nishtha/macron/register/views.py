from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from register.models import *
from register.serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView


class CustomerList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request):
        snippets = Customer.objects.all()
        serializer = CustomerSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class  CustomerDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, phone):
        try:
            snippet = Customer.objects.get(phone=phone)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, phone):
        snippet = self.get_object(phone)
        serializer = CustomerSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, phone):
        snippet = self.get_object(phone=phone)
        serializer = CustomerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, phone):
        snippet = self.get_object(phone)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
