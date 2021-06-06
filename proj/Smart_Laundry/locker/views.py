from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import SmartLocker
from addresses.models import Addresses
from addresses.serializers import AddressesSerializer
from .serializers import SmartLockerSerializer
from .timer import locker_timer

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

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
        locker = SmartLocker.objects.get(pk=pk)
        locker2 = locker.is_locker_reserved
        locker.proximity_sensor = request.data['proximity_sensor']
        locker.lock = request.data['lock']
        if locker2 == request.data['is_locker_reserved']:
            locker.is_user_matched = True            
            locker.save()
            locker_data = SmartLockerSerializer(locker)
            print(locker)
            return Response(locker_data.data)
        else:
            locker.is_user_matched = False
            locker.save()
            locker_data = SmartLockerSerializer(locker)
            return Response(locker_data.data)

    elif request.method == "GET":
        SmartLockers = SmartLocker.objects.get(pk=pk)
        locker_serializers = SmartLockerSerializer(SmartLockers)
        return Response(locker_serializers.data)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def get_data_test(request):
    if request.method == "POST":
        SmartLockers = SmartLockerSerializer(data=request.data)
        s = '111'
        if SmartLockers.is_valid(raise_exception=True):
            SmartLockers.save()
            return Response(request.data)
        
    elif request.method == "GET":
        SmartLockers = SmartLocker.objects.all()
        locker_serializers = SmartLockerSerializer(SmartLocker, many=True)
        return Response(locker_serializers.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def get_detail(request, pk):
    try: 
        locker = SmartLocker.objects.get(pk=pk)
        # print("1", wm.is_wm_reserved)
        locker2 = wm.is_wm_reserved
        
    except SmartLocker.DoesNotExist: 
        return JsonResponse({'message': 'The WashingMachine does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        locker_serializer = SmartLockerSerializer(locker) 
        return Response(wm_serializer.data) 
 
    elif request.method == 'PUT':
        # print("2", wm.is_wm_reserved)
        if locker2 == request.data['is_locker_reserved']:
            locker.is_user_matched = True
            locker.save()
            locker_data = SmartLockerSerializer(locker)
            print(locker)
            return Response(locker_data.data)


    elif request.method == 'DELETE':
        locker.delete() 
        print('delete')
        return Response(status=status.HTTP_204_NO_CONTENT)


class SmartLockerList(APIView):
    """
    목록에 대한 View
    """
    def get(self, request):
        queryset = SmartLocker.objects.all()
        serializer = SmartLockerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SmartLockerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SmartLockerDetail(APIView):
    """
    객체에 대한 View
    """
    def get_object(self, pk):
        return get_object_or_404(SmartLocker, pk=pk)

    def get(self, request, pk):
        locker = self.get_object(pk)
        serializer = SmartLockerSerializer(locker)
        return Response(serializer.data)

    def put(self, request, pk):
        locker = self.get_object(pk)
        serializer = SmartLockerSerializer(locker, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        locker = self.get_object(pk)
        locker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SmartLockerUsing(APIView):
    """
    사물함 사용 유무만 출력
    """
    def get_object(self, pk):
        return get_object_or_404(SmartLocker, pk=pk)

    def get(self, request, pk):
        locker = self.get_object(pk)
        return Response(locker.is_locker_use)


class SmartLockerDoor(APIView):
    """
    사물함 문 개페 상태
    """
    def get_object(self, pk):
        return get_object_or_404(SmartLocker, pk=pk)

    def put(self, request, pk):
        locker = self.get_object(pk)
        serializer = SmartLockerSerializer(locker, data=request.data)

        if serializer.is_valid():
            if locker.proximity_sensor and locker.lock and locker.servo_motor:
                locker.is_locker_door_open = 1
            else:
                locker.is_locker_door_open = 0
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SmartLockerError(APIView):
    """
    사물함 에러 발생 알림
    """
    def get_object(self, pk):
        return get_object_or_404(SmartLocker, pk=pk)

    def put(self, request, pk):
        locker = self.get_object(pk)
        serializer = SmartLockerSerializer(locker, data=request.data)

        if serializer.is_valid():
            if locker.is_locker_door_open:
                # 근접 센서가 고장났을 경우
                if not locker.proximity_sensor:
                    locker.error = 'PE'
                # 잠금 장치가 고장났을 경우
                if not locker.lock:
                    locker.error = 'LE'
                # 서보 모터가 고장났을 경우
                if not locker.servo_motor:
                    locker.error = 'ME'
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SmartLockerUser(APIView):
    """
    Addresses model - email 데이터 가져오기
    """
    def get_object(self, pk):
        return get_object_or_404(Addresses, pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk=pk)
        return Response(user.email)


class SmartLockerTimer(APIView):
    """
    Timer 기능 구현
    """
    def get_object(self, pk):
        return get_object_or_404(Addresses, pk=pk)

    def put(self, request, pk):
        reservation = self.get_object(pk)
        serializer = AddressesSerializer(reservation, data=request.data)

        if serializer.is_valid():
            reservation.Locker_remain_time = locker_timer(reservation.Locker_hour, reservation.Locker_minute, 0)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
