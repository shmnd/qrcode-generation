from django.shortcuts import render,get_object_or_404
from .serializers import FlowerSerializer
from rest_framework.views import APIView
from .models import Flower
from rest_framework import status
from rest_framework.response import Response

# from rest_framework import viewsets

# Create your views here.

# qr code generations

class FlowerList(APIView):         #To list all data and create new data
# To list all data
    def get(self,request):
        queryset=Flower.objects.all()
        serializer=FlowerSerializer(queryset,many=True)
        return Response(serializer.data)
    
# To create a new data
    def post(self,request):
        serializer=FlowerSerializer(data=request.data)        #data converting into json type
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class FlowerData(APIView):        #To list or update or delete a specific item 
#To list a specific item
    def get(self,request,id,format=None):
        flo=get_object_or_404(Flower,pk=id)
        serializer=FlowerSerializer(flo)
        return Response(serializer.data)
   #To update data 
    def put(self,request,id):
        flo=get_object_or_404(Flower,pk=id) #retrive the data from the following id from db(Flower)
        serializer=FlowerSerializer(flo,data=request.data) #provide the data received in the POST request to update the Flower
        serializer.is_valid(raise_exception=True) #Validate the serializer to ensure the provided data is correct and complete
        serializer.save() # Save the updated Flower object with the new data
        return Response(serializer.data,status=status.HTTP_201_CREATED)

#To delete a specific data
    def delete(self,request,id):
        flo=get_object_or_404(Flower,pk=id)
        flo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



    
