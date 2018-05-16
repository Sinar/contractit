# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from hvad.models import TranslatableModel, TranslatedFields

# Create your models here.
class Organization(TranslatableModel):
    id = models.CharField(max_length=255, primary_key=True, blank=True)
    translations = TranslatedFields(
               name = models.CharField(max_length=255) 
            )
    streetAddress = models.CharField(max_length=255, blank=True)
    locality = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255, blank=True)
    postalCode = models.CharField(max_length=20, blank=True)
    countryName = models.CharField(max_length=50, blank=True)

    details = models.CharField(max_length=255, blank=True)
