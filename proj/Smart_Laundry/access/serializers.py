from rest_framework import serializers
from .models import AccessSystem


class AccessSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessSystem
        fields = '__all__'