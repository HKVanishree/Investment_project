from django.conf.urls import url
from . import views

urlpatterns = [
    url('user/', views.registerUser, name='registerUser'),
    url('organization/', views.createOrganizationModel, name='createOrganizationModel'),
    url('investor/', views.createInvestorModel, name='createInvestorModel')
]
