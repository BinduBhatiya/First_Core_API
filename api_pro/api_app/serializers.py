from rest_framework import serializers

class employeeserializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=100) 
