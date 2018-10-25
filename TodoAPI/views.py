from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TodoElements
from .serializers import Todoserializer
class TodoView(APIView):
    def get(self,request):
        print("hi")
        li=TodoElements.objects.all()
        serializer=Todoserializer(li,many=True)

        return Response(serializer.data)
