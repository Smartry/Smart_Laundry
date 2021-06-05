from django.db import models


class AccessSystem(models.Model):
    id = models.AutoField(primary_key=True)
    # 출입문 개폐 상태
    is_access_door_open = models.BooleanField(default=False)
    # 출입문 근접 센서
    proximity_sensor = models.BooleanField(default=False)
    # 출입문 잠금 장치
    locker = models.BooleanField(default=False)
    # 출입문 서보 모터
    servo_motor = models.BooleanField(default=False)
    # 에러 발생 여부
    is_error_occurred = models.BooleanField(default=False)
    # 에러 종류
    error = models.CharField(max_length=20, null=True)
    # 사용자 정부 일치 여부
    is_user_matched = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']