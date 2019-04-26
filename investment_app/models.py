from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from django.core.mail import send_mail


"""Extended python user with added fields isOwner  and isInvestor"""


class newUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    isOwner = models.BooleanField(default=False)
    isInvestor = models.BooleanField(default=False)
    address = models.CharField(max_length=70)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['isOwner', 'isInvestor']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Organization(models.Model):
    organization_id = models.IntegerField()
    organization_name = models.CharField(max_length=30)
    user = models.ManyToManyField(newUser, through='Investment')


class Investment(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(newUser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date_of_investment = models.DateField()


