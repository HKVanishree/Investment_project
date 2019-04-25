# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Owner,Organization,Investor,Investment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OwnerSerializer, OrganizationSerializer,InvestorSerializer
from django.contrib.auth.models import User

# def setOwner(name,owner):
#         owner=Owner.objects.get(user_name=name)


@api_view(["POST", "GET"])
def registerUser(request):
    if request.method == "POST":
      name = request.data.get("username")
      email = request.data.get("email")
      password = request.data.get("password")
      #owner_id=request.data.get("owner_id")
      user = User.objects.create_user(username=name, password=password, email=email)
      Owner.objects.create(user=user)
      return Response({"message": "Owner created"})
    owners = Owner.objects.all()
    serializer = OwnerSerializer(owners, many=True)
    return Response(status=200, data=serializer.data)


@api_view(["POST", "GET"])
def createOrganizationModel(request):
    if request.method == "POST":
      name = request.data.get("organization_name")
      bgt = request.data.get("budget")
      id = request.data.get("owner_id")
      org_id = request.data.get("organization_id")
      owner = Owner.objects.get(pk=id)
      Organization.objects.create(organization_name=name, budget=bgt, owner=owner ,organization_id=org_id)
      return Response({"message": "Organization created"})
    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many=True)
    return Response(status=200, data=serializer.data)


@api_view(["POST", "GET"])
def createInvestorModel(request):
    if request.method == "POST":
        name = request.data.get("investor_name")
        orgkey = request.data.get("organization_id")
        amount = request.data.get("amount")
        invested_date = request.data.get("date_of_investment")
        investor = Investor.objects.create(investor_name=name)
        organisation = Organization.objects.get(organization_id=orgkey)
        Investment.objects.create(amount=amount, date_of_investment=invested_date, investor=investor,
                                  organization=organisation)
        return Response({"message": "Investor created"})
    if request.method == "GET":
        return Response({"message": "Investor created"})








