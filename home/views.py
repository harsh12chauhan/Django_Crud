from django.shortcuts import render
# manually added ======================
from rest_framework.views import APIView
from rest_framework.views import Response

from .serializer import serializer

from .models import userDetails
 
# Create your views here.
class userLists(APIView):

    def get(self,request,id=None):
        if(id is not None):
            try:
                queryset = userDetails.objects.get(id=id)
                serializersData = serializer(queryset)
                return Response(serializersData.data)
            except userDetails.DoesNotExist:  
                return Response({'error':'data not found'},status=400)  
        else:
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
    
    def delete(self,request,id):
        data = userDetails.objects.get(id=id)
        if(data is None):
            return Response({'error':'data not found'},status=400)
        data.delete()
        return Response({'res':'user is deleted '})
    

    def patch(self,request,id=None):
        if id is not None:
            try:
                data = userDetails.objects.get(id=id)       
                serializerData = serializer(data,data=request.data)
                if(serializerData.is_valid()):
                    serializerData.save()            
                    return Response({'res':'data updated successfully'},status=200)
            except userDetails.DoesNotExist:  
                return Response({'error':'data not found'},status=400)
        return Response({'res':'id not found'},status=400)
        

