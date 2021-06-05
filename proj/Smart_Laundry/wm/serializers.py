from rest_framework import serializers
from .models import WashingMachine


class WashingMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WashingMachine
        fields = '__all__'
