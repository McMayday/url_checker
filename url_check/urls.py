from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *


urlpatterns = [
    path('', Main.as_view(), name='main_url'),
    path('ajax/', Ajax_Handler.as_view()),
]
