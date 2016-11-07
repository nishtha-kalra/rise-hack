from rest_framework import serializers
from register.models import Customer


class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    phone = serializers.IntegerField()
    aadhar = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=100)
    account_number = serializers.CharField(max_length=100)
    balance = serializers.IntegerField()
    address = serializers.CharField(max_length=500)
    bank = serializers.CharField(max_length=100)
    geo_location = serializers.CharField(max_length=100)
    language = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Customer.objects.create(**validated_data)
