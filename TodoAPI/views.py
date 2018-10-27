from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TodoElements
from .serializers import Todoserializer
from django.shortcuts import get_object_or_404
class TodoView(APIView):
    def get(self,request):
        li=TodoElements.objects.all()
        serializer=Todoserializer(li,many=True)
        return Response(serializer.data)

    def put(self,request):
        serializer=Todoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class TodoDetailView(APIView):
    def get(self,request,pk):
        li=get_object_or_404(TodoElements,pk=pk)
        serializer=Todoserializer(li,many=False)
        return Response(serializer.data)

    def delete(self,request,pk):
        li=get_object_or_404(TodoElements,pk=pk)
        li.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










