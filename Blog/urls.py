from django.urls import path, include, re_path

from Blog.views import comments, post_form, comment_form

urlpatterns = [
    path('comments/', comments),
    path('post_form/', post_form, name="Post-form"),
    path('comment_form/', comment_form, name="Comment-form"),
]