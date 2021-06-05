from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Addresses
from .serializers import AddressesSerializer
from rest_framework.parsers import JSONParser
from wm.models import WashingMachine
from wm.serializers import WashingMachineSerializer

# from rest_framework.response import Response

# Create your views here.


@csrf_exempt
def address_list(request):
    if request.method == 'GET':
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        # search_name = data['name']
        # obj = Addresses.objects.get(name=search_name)
        # if data['email'] == obj.email:  # 이메일이 같으면 실패
        #     return HttpResponse(status=400)
        # else:  # 이메일이 다르면 가입 가능
        #     if serializer.is_valid():
        #         serializer.save()
        #         return JsonResponse(serializer.data, status=201)

        # wm_reservation_time = data['WM_reservation']
        # if wm_reservation_time < 1000:
        #     '%.04d' % wm_reservation_time
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        # 예약 시간이 12시 이전일 경우 맨 앞자리를 0으로 채우고 싶었으나 실패


@csrf_exempt
def address(request, pk):
    obj = Addresses.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AddressesSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_email = data['email']  # 이메일이 곧 아이디
        obj = Addresses.objects.get(email=search_email)

        if data['password'] == obj.password:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


@csrf_exempt
def reservation(request, pk):
    obj = Addresses.objects.get(pk=pk)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


