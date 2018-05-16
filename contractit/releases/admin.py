# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from hvad.admin import TranslatableAdmin
from releases.models import *


# Register your models here.
class OrganizationAdmin(TranslatableAdmin):
    pass

admin.site.register(Organization, OrganizationAdmin)
