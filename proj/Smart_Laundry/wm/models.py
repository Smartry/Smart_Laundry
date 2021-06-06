from django.db import models


class WashingMachine(models.Model):
    id = models.AutoField(primary_key=True)

    # 세탁기 사용 여부
    is_wm_use = models.BooleanField(default=False)
    # 예약 현황
    is_wm_reserved = models.CharField(max_length=50, null=True)
    # 세탁기 문 개폐 상태
    is_wm_door_open = models.BooleanField(default=False)
    # 세탁기 근접 센서
    proximity_sensor = models.BooleanField(default=False)
    # 세탁기 잠금 장치
    lock = models.BooleanField(default=False)
    # 에러 발생 여부
    is_error_occurred = models.BooleanField(default=False)
    # 에러 종류
    error = models.CharField(max_length=20, null=True)
    # 사용자 정보 일치 여부
    is_user_matched = models.BooleanField(default=False)
    # 세탁 옵션 정보
    wm_options = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['id']