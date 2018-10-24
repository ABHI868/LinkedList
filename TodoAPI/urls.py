
from TodoAPI.views import TodoView

from django.conf.urls import url
from django.urls import path

url_patterns=[

    path('api/',TodoView.as_view()),




]