from django.urls import path
from .views import index,do_task

urlpatterns = [
    path('',index,name='index'),
    path('task/',do_task,name='task'),
]
