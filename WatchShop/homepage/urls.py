from django.contrib import admin
from django.urls import path
from .views import Home, About,Upload

urlpatterns = [
    path('', Home , name ="home"),
    path('about', About , name ="about"),
    path('upload', Upload, name="upload")
]
