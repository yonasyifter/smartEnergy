# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import EnergyMeter
from tinymce.widgets import TinyMCE
from django.db import models

class SEMeter(admin.ModelAdmin):
    list_display = ('full_name', 'house_number', 'reading', 'payment')
# Register your models here.
admin.site.register(EnergyMeter, SEMeter)
