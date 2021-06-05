from django.db import models

# Create your models here.


class Addresses(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=10, null=True)
    phone_number = models.CharField(max_length=13, null=True)
    address = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    password = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=30, null=True)
    identification = models.CharField(max_length=10, null=True)
    mem_point = models.IntegerField(null=True)
    sex = models.IntegerField(null=True)
    # 세탁 예약 시간
    WM_hour = models.IntegerField(null=True)
    WM_minute = models.IntegerField(null=True)
    WM_remain_time = models.CharField(null=True, max_length=10)
    # 사물함 예약 시간
    Locker_hour = models.IntegerField(null=True)
    Locker_minute = models.IntegerField(null=True)
    Locker_remain_time = models.CharField(null=True, max_length=10)

    class Meta:
        ordering = ['id']
