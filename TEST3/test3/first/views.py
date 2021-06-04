from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Sensor
from .serializers import SensorSerializer

from rest_framework import viewsets
from rest_framework.decorators import action 


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    @action(detail=True, methods=['post'])
    def get_data(self, request, pk=None):
        # return Response({'numbers': 'test'})
        return Response({'numbers': 'test', 'servo': 'test1', 'code': 'test2'})
# 

        # return Response(serializer.data)
#     @action(detail=True, methods=['post'])
#     def set_servo(self, request, pk=None):
#         user = self.get_object()
#         serializer = SensorSerializer(data=request.data)
#         if serializer.is_valid():
#             user.set_servo(serializer.data['servo'])
#             user.save()
#             return Response({'status': 'servo set'})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     serializer = SensorSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = SensorSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)

post_list = SensorViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
# class ServoList(APIView):
#     """
#     목록에 대한 View
#     """
#     def get(self, request):
#         queryset = Sensor.objects.all()
#         serializer = SensorSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = SensorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)