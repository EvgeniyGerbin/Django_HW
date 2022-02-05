from django.urls import path, include, re_path
from myapp.views import first

urlpatterns = [
    path('some_url/', first, name='first')
]