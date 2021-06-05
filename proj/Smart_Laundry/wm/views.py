from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import WashingMachine
from addresses.models import Addresses
from addresses.serializers import AddressesSerializer
from .serializers import WashingMachineSerializer
from .timer import laundry_timer

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

# from .models import WashingMachine
# from .serializers import WashingMachineSerializer

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
        wm = WashingMachine.objects.get(pk=pk)
        print("1", wm.is_wm_reserved)
        wm2 = wm.is_wm_reserved
        if wm2 == request.data['is_wm_reserved']:
            wm.is_user_matched = True
            wm.save()
            wm_data = WashingMachineSerializer(wm)
            print(wm)
            return Response(wm_data.data)
        else:
            wm.is_user_matched = False
            wm.save()
            wm_data = WashingMachineSerializer(wm)
            return Response(wm_data.data)
        # if wm_serializers.is_valid(raise_exception=True):
        #     wm_serializers.save()
        #     return Response(s)
        
    elif request.method == "GET":
        WashingMachines = WashingMachine.objects.all()
        wm_serializers = WashingMachineSerializer(WashingMachines, many=True)
        return Response(wm_serializers.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def get_detail(request, pk):
    try: 
        # WashingMachine = WashingMachine.objects.all()
        wm = WashingMachine.objects.get(pk=pk)
        print("1", wm.is_wm_reserved)
        wm2 = wm.is_wm_reserved
        # wm2 = WashingMachine.objects.get(pk=pk)
        
    except WashingMachine.DoesNotExist: 
        return JsonResponse({'message': 'The WashingMachine does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        wm_serializer = WashingMachineSerializer(wm) 
        return Response(wm_serializer.data) 
 
    elif request.method == 'PUT':
        print("2", wm.is_wm_reserved)
        if wm2== request.data['is_wm_reserved']:
            wm.is_user_matched = True
            wm.save()
            wm_data = WashingMachineSerializer(wm)
            print(wm)
            return Response(wm_data.data)

        #wm_data = JSONParser().parse(request) 
        #wm_serializer = WashingMachineSerializer(wm, data=wm_data)
        # if wm_serializer.is_valid():
        #print("3", wm.is_wm_reserved)
                
        #if wm_serializer.is_valid():
            # wm_serializer.save()
            #print("4_1", wm.is_wm_reserved)
            # wm_instance = wm_serializer.save()
            #wm_instance = wm_serializer.save(wm_serializer.data['is_wm_reserved'])
            # print("4", wm.is_wm_reserved)
            # print("INSTANCE", wm_instance.is_wm_reserved)
            # # print(wm_instance)
            # post = PostCreateSerializer(data=request.data, context={'request': request})
            # post.is_valid(raise_excpetions=True)
            # post_instance = post.save()
            # media_url = post_instance.media.url
            # link = find_link_value()
            # post_instance.link = link
            # post_instance.save()

            # if wm_serializer.validated_data:
            #print(wm.is_wm_reserved, wm2)
            # if wm.is_wm_reserved == wm2.is_wm_reserved:
                # print("YES!")
            # else:
                # print("NO!")
            # print(wm_serializer.data['is_wm_reserved'] == wm2.is_wm_reserved)
            # if wm_serializer.data['is_wm_reserved'] == wm2.is_wm_reserved:
            # if wm_serializer.data['is_wm_reserved'] == wm2:
            # # if wm_instance.is_wm_reserved == wm2:
            #     print("5", wm.is_wm_reserved)
            #     print('True!!!!!!!!!')
            #     # wm_instance.save()
            #     # wm_instance.is_user_matched = True
            #     wm.is_user_matched = True
            #     wm_instance.save()
            #     print("6", wm.is_wm_reserved)

            #     return Response(wm_serializer.data)
                # return Response(wm_instance.data)  
        #     #wm_serializer.data['is_user_matched'] = True
        #     wm_serializer2 = WashingMachineSerializer(wm)
        #     if wm_serializer2.is_valid():
        #         wm_serializer2.save()

                # wm_serializer.data['is_user_matched'] = True
                # wm_serializer = WashingMachineSerializer(wm)
                # wm.is_user_matched = True
                # return Response(wm.is_user_matched)    
                # wm_serializer.save() 
                # return Response(wm_serializer.data)       
                # return Response(wm)   
        else:
            str = "False!!!!!!"
            # wm.is_user_matched = False
            # print("7", wm.is_wm_reserved)
            return Response(str)

        
            # print(wm_serializer.data['is_wm_reserved'])
            # print(type(wm_serializer.data['is_wm_reserved']))
            # print(wm.is_wm_reserved)
            # print(type(wm.is_wm_reserved))
            
            # return Response(wm_serializer.data)    
                # wm_serializer.save() 
            #print(type(wm))
        #return Response(type(wm))      
        #return Response(wm_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        # return Response("is wm matched") 
 
    elif request.method == 'DELETE':
        wm.delete() 
        print('delete')
        return Response(status=status.HTTP_204_NO_CONTENT)




class WashingMachineList(APIView):
    """
    목록에 대한 View
    """
    def get(self, request):
        queryset = WashingMachine.objects.all()
        serializer = WashingMachineSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WashingMachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class WashingMachineDetail(APIView):
    """
    객체에 대한 View
    """
    def get_object(self, pk):
        return get_object_or_404(WashingMachine, pk=pk)

    def get(self, request, pk):
        wm = self.get_object(pk)
        serializer = WashingMachineSerializer(wm)
        return Response(serializer.data)

    def put(self, request, pk):
        wm = self.get_object(pk)
        serializer = WashingMachineSerializer(wm, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        wm = self.get_object(pk)
        wm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WashingMachineUsing(APIView):
    """
    세탁기 사용 유무만 출력
    """
    def get_object(self, pk):
        return get_object_or_404(WashingMachine, pk=pk)

    def get(self, request, pk):
        wm = self.get_object(pk)
        return Response(wm.is_wm_use)


class WashingMachineDoor(APIView):
    """
    세탁기 문 개폐 상태
    """
    def get_object(self, pk):
        return get_object_or_404(WashingMachine, pk=pk)

    def put(self, request, pk):
        wm = self.get_object(pk)
        serializer = WashingMachineSerializer(wm, data=request.data)

        if serializer.is_valid():
            if wm.proximity_WashingMachine and wm.lock and wm.servo_motor:
                wm.is_wm_door_open = 1
            else:
                wm.is_wm_door_open = 0
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WashingMachineError(APIView):
    """
    세탁기 에러 발생 알림
    """
    def get_object(self, pk):
        return get_object_or_404(WashingMachine, pk=pk)

    def put(self, request, pk):
        wm = self.get_object(pk)
        serializer = WashingMachineSerializer(wm, data=request.data)

        if serializer.is_valid():
            if wm.is_wm_door_open:
                # 근접 센서가 고장났을 경우
                if not wm.proximity_WashingMachine:
                    wm.error = 'PE'
                # 잠금 장치가 고장났을 경우
                if not wm.lock:
                    wm.error = 'LE'
                # 서보모터가 고장났을 경우
                if not wm.servo_motor:
                    wm.error = 'ME'
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WashingMachineUser(APIView):
    """
    Addresses model - email 데이터 가져오기
    """
    def get_object(self, pk):
        return get_object_or_404(Addresses, pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk=pk)
        return Response(user.email)
    
    
class WashingMachineTimer(APIView):
    """
    Timer 기능 구현
    """
    def get_object(self, pk):
        return get_object_or_404(Addresses, pk=pk)

    def put(self, request, pk):
        reservation = self.get_object(pk)
        serializer = AddressesSerializer(reservation, data=request.data)

        if serializer.is_valid():
            reservation.WM_remain_time = laundry_timer(reservation.WM_hour, reservation.WM_minute, 0)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
