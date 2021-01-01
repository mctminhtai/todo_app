from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='list'),
    path('update_task/<str:pk>/',updatetask, name='update_task'),
    path('delete_task/<str:pk>/',deletetask,name='delete_task'),
]