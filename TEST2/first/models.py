# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sensor(models.Model):
    servo = models.CharField(max_length=50, null=True)