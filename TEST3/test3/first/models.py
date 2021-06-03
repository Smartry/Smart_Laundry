from django.db import models

# Create your models here.
class Sensor(models.Model):
    servo = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=500, null=True)