import imp
from django.contrib import admin
from django.urls import path,include, re_path
from about import views
from django.urls import re_path as url

urlpatterns =   [
    url(r'about/', views.about),
]