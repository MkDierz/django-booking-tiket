from django.conf.urls import include
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('',include('blog.urls')),
    path('',include('about.urls')),
    path('',include('contact.urls')),
]