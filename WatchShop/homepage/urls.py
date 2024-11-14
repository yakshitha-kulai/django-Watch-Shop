from django.contrib import admin
from django.urls import path
from .views import Home, About,Upload, login_user, logout_user, signup_user

urlpatterns = [
    path('', Home , name ="home"),
    path('about', About , name ="about"),
    path('upload', Upload, name="upload"),
    path('login', login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path('signup', signup_user, name="signup")

]
