from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import biller
from . serializers import *

class billerList(APIView):
    def get(self, request):
        biller1=biller.objects.all()
        return Response(billerSerializers(biller1, many=True).data)

    def post(self):
        pass

class billerList2(APIView):
    def get(self, request):
        biller1=biller.objects.all()
        return Response(billerSerializers2(biller1, many=True).data)

    def post(self):
        pass

class billerList3(APIView):
    def get(self, request):
        biller1=biller.objects.all()
        return Response(billerSerializers3(biller1, many=True).data)

    def post(self):
        pass
class billerList4(APIView):
    def get(self, request):
        biller1=biller.objects.all()
        return Response(billerSerializers4(biller1, many=True).data)

    def post(self):
        pass


# Create your views here.
