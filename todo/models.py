# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TodoTable(models.Model):
    title=models.CharField(max_length=30, null=True, blank=True)
    description=models.TextField(max_length=250, null=True, blank=True)
    #created_time=models.DateTimeField(auto_now_add=True)