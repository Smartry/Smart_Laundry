from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import AccessSystem
from .serializers import AccessSystemSerializer
from addresses.models import Addresses


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