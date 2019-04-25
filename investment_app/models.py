from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    isOwner = models.BooleanField()
    isInvestor = models.BooleanField()

    objects = UserManager()


class Owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # owner_id = models.IntegerField()
    # owner_name = models.CharField(max_length=30)
    # email = models.EmailField()


class Organization(models.Model):
    organization_id = models.IntegerField()
    organization_name = models.CharField(max_length=30)
    budget = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Investor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # investor_name = models.CharField(max_length=30)
    organization = models.ManyToManyField(Organization, through='Investment')


class Investment(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date_of_investment = models.DateField()
