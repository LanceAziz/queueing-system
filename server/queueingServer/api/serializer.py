from rest_framework import serializers
from .models import Client, Teller

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class TellerSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Teller
        fields = '__all__'