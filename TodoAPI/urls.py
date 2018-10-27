
from .views import TodoView,TodoDetailView

from django.conf.urls import url
from django.urls import path

urlpatterns=[

    # path('api/$',TodoView.as_view()),
    path('',TodoView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',TodoDetailView.as_view())


]