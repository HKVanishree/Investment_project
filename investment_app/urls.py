from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('user/', views.registerUser, name='registerUser'),
    url('organization/', views.createOrganizationModel, name='createOrganizationModel'),
    url('invest/', views.createInvestmentModel, name='createInvestmentModel'),
    path('investors/<int:org_id>/', views.getInvestorsOfAnOrganization),
    path('organizations/<int:owner_id>/', views.getOrganizationsOfAnOwner)
]
