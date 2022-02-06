from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Blog.models import CommentPost
from Blog.forms import PostForm, CommentForm


def comments(request: HttpRequest) -> HttpResponse:
    comments = CommentPost.objects.all()[::-1][:5]
    context = {
        'objects': comments

    }

    return render(request, 'comments.html', context)


def post_form(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/post_form')
    return render(request, 'post_form.html', {'form': form})

def comment_form(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect('/comment_form')
    return render(request, 'comment_form.html', {'comment_form': comment_form})
