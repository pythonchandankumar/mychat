from django.urls import path
from .views import *

urlpatterns = [
    path('',lobby,name='lobby'),
    path("room/",room,name='room'),
    
]
