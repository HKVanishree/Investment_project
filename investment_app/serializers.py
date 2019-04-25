from rest_framework import serializers
from .models import *


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    #owners = OwnerSerializer(many=True)
    #investors = InvestorSerializer(many=True)

    class Meta:
        model = Organization
        fields = '__all__'


class InvestmentSerializer(serializers.ModelSerializer):
    investors = InvestorSerializer(read_only=True)

    class Meta:
        model = Investment
        fields = '__all__'


# class ModelSerializer(serializers.Serializer):
#     owner_name = serializers.CharField()
#     email = serializers.EmailField()
#     fields = ('owner_name', 'email')
