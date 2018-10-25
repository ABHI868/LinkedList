from django.db import models

# Create your models here.

class TodoElements(models.Model):
    todo_text=models.CharField(max_length=300)
    done=models.BooleanField()
 