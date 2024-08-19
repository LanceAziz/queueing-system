from rest_framework import serializers
from .models import Client, Teller

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
