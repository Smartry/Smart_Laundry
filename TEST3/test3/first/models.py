from django.db import models

# Create your models here.
class Sensor(models.Model):
    numbers = models.CharField(max_length=500, null=True)
    servo = models.CharField(max_length=500, null=True)
    code = models.CharField(max_length=500, null=True)