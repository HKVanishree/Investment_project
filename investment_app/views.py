from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, OrganizationSerializer, InvestmentSerializer
from .models import newUser, Organization, Investment
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(["POST", "GET"])
def registerUser(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        isOwner = request.data.get("isOwner")
        isInvestor = request.data.get("isInvestor")
        address = request.data.get("address")
        newUser.objects.create_user(email, password, isInvestor, isOwner, address)
        return Response({"message": "Owner created"})
    if request.method == "GET":
        users = newUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(status=200, data=serializer.data)


@api_view(["POST", "GET"])
def createOrganizationModel(request):
    if request.method == "POST":
        name = request.data.get("organization_name")
        bgt = request.data.get("budget")
        owner_id = request.data.get("owner_id")
        org_id = request.data.get("organization_id")
        user = newUser.objects.get(pk=owner_id)
        if user.isOwner:
            Organization.objects.create(organization_name=name, budget=bgt, user=user, organization_id=org_id)
            return Response("Organization created")
        else:
            return Response("Not a Owner")
    if request.method == "GET":
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(status=200, data=serializer.data)


@api_view(["POST", "GET"])
def createInvestmentModel(request):
    if request.method == "POST":
        investor_id = request.data.get("investor_id")
        organization_id = request.data.get("organization_id")
        amount = request.data.get("amount")
        invested_date = request.data.get("date_of_investment")
        investor = newUser.objects.get(pk=investor_id)
        if investor.isInvestor:
            organization = Organization.objects.get(organization_id=organization_id)
            Investment.objects.create(amount=amount, date_of_investment=invested_date, user=investor,
                                      organization=organization)
            return Response({"message": "Investor created"})
        else:
            return Response(status=404, data="Not an investor")
    if request.method == "GET":
        investment = Investment.objects.all()
        serializer = InvestmentSerializer(investment, many=True)
        return Response(status=200, data=serializer.data)


@api_view(["GET"])
def getInvestorsOfAnOrganization(request, org_id):
    #orgId=5
    organization = Organization.objects.get(organization_id=org_id)
    investors = organization.user.all()
    serializer = UserSerializer(investors, many=True)
    return Response(status=200, data=serializer.data)

@api_view(["GET"])
def getOrganizationsOfAnOwner(request, owner_id):
    owner = newUser.objects.get(pk=owner_id)
    organizations = Organization.objects.filter(user=owner)
    serializer = OrganizationSerializer(organizations, many=True)
    return Response(status=200, data=serializer.data)







