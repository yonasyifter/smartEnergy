# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Code
# Create your views here.
def home(request):
    #data = Energy.objects.filter(amount)
    code = Code.objects.all()
    context= {
     'code': code
    }
    return render(request, 'smartEnergyMeter/home.html', context)
