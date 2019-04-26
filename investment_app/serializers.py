from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = newUser
        fields = ('id', 'email', 'address')


class OrganizationSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=True)

    class Meta:
        model = Organization
        fields = '__all__'


class InvestmentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    organization = OrganizationSerializer()

    class Meta:
        model = Investment
        fields = '__all__'
