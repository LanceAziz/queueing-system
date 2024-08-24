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
        # fields = ["id","username","password","num","type"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        teller = Teller.objects.create_user(**validated_data)
        return teller
    
class TextSerializer(serializers.Serializer):
    text = serializers.CharField()