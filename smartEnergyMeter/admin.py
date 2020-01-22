# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Code
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class CAdmin(admin.ModelAdmin):
    fieldsets = [('Title and Date',{'fields':['title','date']}),
                 ('Content Block',{'fields':['code']})]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Code,CAdmin)
