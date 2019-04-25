# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from investment_app.models import Owner
from .models import Organization
from .models import Investment
from .models import Investor

admin.site.register(Owner)
admin.site.register(Investment)
admin.site.register(Organization)
admin.site.register(Investor)


