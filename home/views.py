from django.shortcuts import render
# manually added ======================
from rest_framework.views import APIView
from rest_framework.views import Response

from .serializer import serializer

from .models import userDetails

import json


# Create your views here.
class userLists(APIView):
    def get(self,request):
        queryset = userDetails.objects.all()
        serializersData = serializer(queryset,many=True) 
        return Response(serializersData.data)
    
    def post(self,request):
        data = request.data
        serializerData = serializer(data=data)
        if(serializerData.is_valid()):
            serializerData.save()
            return Response(data)
        return Response(status=400)

