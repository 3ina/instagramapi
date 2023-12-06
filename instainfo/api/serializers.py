from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    username = serializers.CharField()