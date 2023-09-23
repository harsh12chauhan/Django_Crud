from django.shortcuts import render

# importing restframework
from rest_framework.views import APIView
from rest_framework.views import Response
# models
from .models import details
# serializer
from .serializer import serializerDetails


# Create your views here.
class moreDetails(APIView):

    def get(self,request,id=None):
        if(id is not None):
            try:
                data = details.objects.get(id=id)
                serializerData = serializerDetails(data)
                return Response(serializerData.data)
            except details.DoesNotExist:
                return Response({'res':'no data found'},status=400)
        else:
            data = details.objects.all()
            serializerData = serializerDetails(data,many=True)
            return Response(serializerData.data)
        
    def post(self,request):
        data = request.data
        if(data):
            serializerData = serializerDetails(data=data)
            if(serializerData.is_valid()):
                serializerData.save()
                return Response(serializerData.data)
        return Response({'res':'data not fonud'},status=400)
    
    def delete(self,request,id):
        data = details.objects.get(id=id)
        if (data is None):
            return Response({'error':'id not found'},status=400)
        data.delete()
        return Response({'res':'data deleted successfully'},status=200)
    
    def patch(self,request,id):
        if(id is not None):
            try:                
                data = details.objects.get(id=id)
                serializerData = serializerDetails(data,data = request.data,partial=True)
                if(serializerData.is_valid()):
                    serializerData.save()
                    return Response({'res':'updated successfully'},status=200)
            except details.DoesNotExist:
                return Response({'res':'not updated'},status=400)
        return Response({'res':'id not found'},status=400)


    




