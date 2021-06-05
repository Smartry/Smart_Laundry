from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import SmartLocker
from addresses.models import Addresses
from addresses.serializers import AddressesSerializer
from .serializers import SmartLockerSerializer
from .timer import locker_timer


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
