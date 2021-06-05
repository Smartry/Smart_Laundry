from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Sensor
from .serializers import SensorSerializer

from rest_framework import viewsets
from rest_framework.decorators import action 

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def get_data(request):
    if request.method == "POST":
        sensor_serializers = SensorSerializer(data=request.data)
        s = '111'
        if sensor_serializers.is_valid(raise_exception=True):
            sensor_serializers.save()
            return Response(s)
        print('ddddd')
    elif request.method == "GET":
        sensors = Sensor.objects.all()
        sensor_serializers = SensorSerializer(sensors, many=True)
        return Response(sensor_serializers.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def get_detail(request, pk):
    try: 
        # sensor = Sensor.objects.all()
        sensor = Sensor.objects.get(pk=pk)
    except Sensor.DoesNotExist: 
        return JsonResponse({'message': 'The sensor does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        sensor_serializer = SensorSerializer(sensor) 
        return Response(sensor_serializer.data) 
 
    elif request.method == 'PUT': 
        sensor_data = JSONParser().parse(request) 
        sensor_serializer = SensorSerializer(sensor, data=sensor_data) 
        if sensor_serializer.is_valid(): 
            sensor_serializer.save() 
            return JsonResponse(sensor_serializer.data) 
        return JsonResponse(sensor_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE':
        sensor.delete() 
        print('delete')
        return Response(status=status.HTTP_204_NO_CONTENT)