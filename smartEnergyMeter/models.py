# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
class Code(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.title
