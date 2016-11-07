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
from random import randint
from twilio.rest import TwilioRestClient

'''
class CustomerList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request):
        snippets = Customer.objects.all()
        serializer = CustomerSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        print "in post"
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''


@api_view(['GET', 'POST'])
def details(request):
    """
    List all snippets, or create a new snippet.
    """
    print request.method
    if request.method == 'GET':
        snippets = Customer.objects.all()
        serializer = CustomerSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            account = "ACbf3b4c740e56b12a8f8c26bd1ecb9c71"
            token = "2d491e1876e879d05c27b14a0f0e166c"
            client = TwilioRestClient(account, token)
            otp = str(randint(1000,2000))
            print "data:"
            data = serializer.data
            print data
            print "phone:"
            phone_number = '+' + str(data['phone'])
            print "phone:"
            print phone_number
            message = client.sms.messages.create(to=phone_number,from_="+1 720-439-3905",body="Your otp is" + otp)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print "errors:"
        print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
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


@api_view(['GET', 'POST'])
def send_otp(self, request):
    data = request.data
    print "data:"
    print data
    account = "ACbf3b4c740e56b12a8f8c26bd1ecb9c71"
    token = "2d491e1876e879d05c27b14a0f0e166c"
    client = TwilioRestClient(account, token)
    otp = randint(1000,2000)
    return Response(otp)
