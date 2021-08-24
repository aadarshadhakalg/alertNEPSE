from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import ObtainAuthToken
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('sign-in/',ObtainAuthToken.as_view()),
    path('change-password/',ChangePasswordView.as_view()),
]