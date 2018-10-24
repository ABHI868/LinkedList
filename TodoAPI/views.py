from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class TodoView(APIView):
    def get(self,request):
        print("hi")
        return Response({"name":"abhishek"})
