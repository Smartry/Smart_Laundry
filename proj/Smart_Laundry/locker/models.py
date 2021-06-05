from django.db import models


class SmartLocker(models.Model):
    id = models.AutoField(primary_key=True)

    # 사물함 사용 여부
    is_locker_use = models.BooleanField(default=False)
    # 예약 현황
    is_locker_reserved = models.BooleanField(default=False)
    # 사물함 문 개폐 상태
    is_locker_door_open = models.BooleanField(default=False)
    # 사물함 근접 센서
    proximity_sensor = models.BooleanField(default=False)
    # 사물함 잠금 장치
    lock = models.BooleanField(default=False)
    # 사물함 서보 모터
    servo_motor = models.BooleanField(default=False)
    # 에러 발생 여부
    is_error_occurred = models.BooleanField(default=False)
    # 에러 종류
    error = models.CharField(max_length=20, null=True)
    # 사용자 정보 일치 여부
    is_user_matched = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
