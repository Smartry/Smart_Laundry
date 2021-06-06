from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import AccessSystem
from .serializers import AccessSystemSerializer
from addresses.models import Addresses

from rest_framework import viewsets
from rest_framework.decorators import action 

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def get_data(request, pk):
    if request.method == "POST":
        access = AccessSystem.objects.get(pk=pk)
        print("1", access.smartry_id)
        access2 = access.smartry_id
        access.proximity_sensor = request.data['proximity_sensor']
        access.lock = request.data['lock']
        access.servo_motor = request.data['servo_motor']

        if access2 == request.data['smartry_id']:
            access.is_user_matched = True            
            access.save()
            access_data = AccessSystemSerializer(access)
            print(access)
            return Response(access_data.data)
        else:
            access.is_user_matched = False
            access.save()
            access_data = AccessSystemSerializer(access)
            return Response(access_data.data)

    elif request.method == "GET":
        AccessSystems = AccessSystem.objects.get(pk=pk)
        access_serializers = AccessSystemSerializer(AccessSystems)
        return Response(access_serializers.data)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def get_data_test(request):
    if request.method == "POST":
        access_serializers = AccessSystemSerializer(data=request.data)
        if access_serializers.is_valid(raise_exception=True):
            access_serializers.save()
            return Response(request.data)
        
    elif request.method == "GET":
        AccessSystems = AccessSystem.objects.all()
        access_serializers = AccessSystemSerializer(AccessSystems, many=True)
        return Response(access_serializers.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def get_detail(request, pk):
    try: 
        # AccessSystem = AccessSystem.objects.all()
        access = AccessSystem.objects.get(pk=pk)
        print("1", access.smartry_id)
        access2 = access.smartry_id
        # access2 = AccessSystem.objects.get(pk=pk)
        
    except AccessSystem.DoesNotExist: 
        return JsonResponse({'message': 'The AccessSystem does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        access_serializer = AccessSystemSerializer(access) 
        return Response(access_serializer.data) 
 
    elif request.method == 'PUT':
        print("2", access.smartry_id)
        if access2== request.data['smartry_id']:
            access.is_user_matched = True
            access.save()
            access_data = AccessSystemSerializer(access)
            print(access)
            return Response(access_data.data)


    elif request.method == 'DELETE':
        access.delete() 
        print('delete')
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccessSystemList(APIView):
    """
    목록에 대한 View
    """
    def get(self, request):
        queryset = AccessSystem.objects.all()
        serializer = AccessSystemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccessSystemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AccessSystemDetail(APIView):
    """
    객체에 대한 View
    """
    def get_object(self, pk):
        return get_object_or_404(AccessSystem, pk=pk)

    def get(self, request, pk):
        access = self.get_object(pk)
        serializer = AccessSystemSerializer(access)
        return Response(serializer.data)

    def put(self, request, pk):
        access = self.get_object(pk)
        serializer = AccessSystemSerializer(access, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        access = self.get_object(pk)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccessSystemDoor(APIView):
    """
    출입문 개폐 상태
    """
    def get_object(self, pk):
        return get_object_or_404(AccessSystem, pk=pk)

    def put(self, request, pk):
        access = self.get_object(pk)
        serializer = AccessSystemSerializer(access, data=request.data)

        if serializer.is_valid():
            if access.proximity_sensor and access.locker and access.servo_motor:
                access.is_access_door_open = 1
            else:
                access.is_access_door_open = 0
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccessSystemError(APIView):
    """
    출입문 에러 발생 알림
    """
    def get_object(self, pk):
        return get_object_or_404(AccessSystem, pk=pk)

    def put(self, request, pk):
        access = self.get_object(pk)
        serializer = AccessSystemSerializer(access, data=request.data)

        if serializer.is_valid():
            if access.is_access_door_open:
                # 근접 센서가 고장났을 경우
                if not access.proximity_sensor:
                    access.error = 'PE'
                # 잠금 장치가 고장났을 경우
                if not access.locker:
                    access.error = 'LE'
                # 서보모터가 고장났을 경우
                if not access.servo_motor:
                    access.error = 'ME'
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccessSystemUser(APIView):
    """
    Addresses model - email 데이터 가져오기
    """
    def get_object(self, pk):
        return get_object_or_404(Addresses, pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk=pk)
        return Response(user.email)