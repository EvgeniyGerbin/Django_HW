
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path

from myapp.views import *

urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('', include('Blog.urls'), name='comments')


    # path('acricles/', acricles),
    # path('acricles/archive/', acricles_archive),
    # path('users/', users),
    # path('article/<int:article_id>/', article_number),
    # path('article/<int:article_id>/archive/', article_number),
    # path('article/<int:article_id>/<slug:slug_text>/', article_number_someText),
    # path('users/<int:user_id>/', users_number),
    # re_path('(0(50|63|95|96)([0-9]{7}))', phone_number),
    # re_path('[a-f1-9]{4}-\w{6}', regex),

]
