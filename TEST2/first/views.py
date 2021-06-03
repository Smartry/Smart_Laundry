# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Servo
from .serializers import ServoSerializer


class ServoList(APIView):
    """
    목록에 대한 View
    """
    def get(self, request):
        queryset = Servo.objects.all()
        serializer = ServoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)