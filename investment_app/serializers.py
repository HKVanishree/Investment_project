from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = newUser
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)

    class Meta:
        model = Organization
        fields = '__all__'


class InvestmentSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    organization = OrganizationSerializer()

    class Meta:
        model = Investment
        fields = '__all__'
