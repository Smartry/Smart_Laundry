from rest_framework import serializers
from .models import SmartLocker


class SmartLockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartLocker
        fields = '__all__'