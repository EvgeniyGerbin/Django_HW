
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path

from Blog.views import comments


urlpatterns = [
    path('comments/', comments),
]