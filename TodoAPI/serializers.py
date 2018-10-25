from rest_framework import serializers
from .models import TodoElements

class Todoserializer(serializers.ModelSerializer):
    class Meta:
    
        model =TodoElements
        fields='id','todo_text','done'