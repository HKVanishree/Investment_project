# from django.contrib.auth.base_user import BaseUserManager
#
#
# class UserManager(BaseUserManager):
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(email, password, **extra_fields)


from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, password, isInvestor, isOwner, address):
        user = self.model(email=email, password=password, isInvestor=isInvestor, isOwner=isOwner, address=address)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, isInvestor, isOwner):
        user = self.create_user(email=email, password=password, isInvestor=isInvestor, isOwner=isOwner)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)

