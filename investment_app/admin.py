# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import newUser
from .models import Organization
from .models import Investment


admin.site.register(newUser)
admin.site.register(Investment)
admin.site.register(Organization)



