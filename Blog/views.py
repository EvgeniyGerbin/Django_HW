from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from Blog.models import CommentPost


def comments(request: HttpRequest) -> HttpResponse:
    comments = CommentPost.objects.all()[::-1][:5]
    context = {
        'objects': comments

    }

    return render(request, 'comments.html', context)
