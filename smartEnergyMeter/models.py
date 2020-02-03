# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class EnergyMeter(models.Model):
    full_name = models.CharField(max_length=100)
    house_number = models.TextField()
    reading = models.FloatField()
    payment = models.FloatField()

    class Meta:
        ordering = ('payment',)
        verbose_name_plural = 'EnergyMeter'

    def __str__(self):
        return self.full_name
