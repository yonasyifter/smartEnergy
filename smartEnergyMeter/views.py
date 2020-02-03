# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import EnergyMeter
from .forms import LogIn

# Create your views here.
def home(request):
    form = LogIn(request.POST)
    return render(request, 'smartEnergyMeter/login.html', context={'form': form})
