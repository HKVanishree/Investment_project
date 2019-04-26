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
       try:
        name = request.data.get("organization_name")
        bgt = request.data.get("budget")
        owner_id = request.data.get("owner_id")
        org_id = request.data.get("organization_id")
        user = newUser.objects.get(pk=owner_id)
       except:
           return Response({'error':'Could not register Organization due to null fields'},status=400)
       if user.isOwner:
           try:
            Organization.objects.create(organization_name=name, budget=bgt, user=user, organization_id=org_id)
            return Response("Organization created")
           except:
               return Response("Organization not created")
       else:
            return Response("Not a Owner")
    if request.method == "GET":
        try:
            organizations = Organization.objects.all()
        except:
            return Response(status=404, data="Could not retrieve list of organizations")
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(status=200, data=serializer.data)





@api_view(["POST", "GET"])
def createInvestmentModel(request):
    if request.method == "POST":
        try:
            investor_id = request.data.get("investor_id")
            organization_id = request.data.get("organization_id")
            amount = request.data.get("amount")
            invested_date = request.data.get("date_of_investment")
            investor = newUser.objects.get(pk=investor_id)
        except:
            return Response(status=404, data="Could not create investors due to null fields")
        if investor.isInvestor:
            try:
                organization = Organization.objects.get(organization_id=organization_id)
                Investment.objects.create(amount=amount, date_of_investment=invested_date, user=investor,
                                          organization=organization)
                return Response({"message": "Investor created"})
            except:
                Response({"message": "Investor not created"})
        else:
            return Response(status=404, data="Not an investor")
    if request.method == "GET":
        try:
            investment = Investment.objects.all()
            serializer = InvestmentSerializer(investment, many=True)
            return Response(status=200, data=serializer.data)
        except:
            return Response(status=404, data="Could not retrieve list of investors")



@api_view(["GET"])
def getInvestorsOfAnOrganization(request, org_id):
    try:
        organization = Organization.objects.get(organization_id=org_id)
        investors = organization.user.all()
        serializer = UserSerializer(investors, many=True)
        return Response(status=200, data=serializer.data)
    except:
        return Response(status=404, data="Could not retrieve list of investors")


@api_view(["GET"])
def getOrganizationsOfAnOwner(request, owner_id):
    owner = newUser.objects.get(pk=owner_id)
    organizations = Organization.objects.filter(user=owner)
    serializer = OrganizationSerializer(organizations, many=True)
    return Response(status=200, data=serializer.data)





