from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.
class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')

    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
        'now': datetime.now(),

    })



def first(request):
    return render(request, 'first.html', {
        'now': datetime.now(),
    })


def another(request):
    return HttpResponse("It's another page!!")


def acricles(HttpRequest) -> HttpResponse:
    return HttpResponse("ACRICLES!!!")


def acricles_archive(HttpRequest) -> HttpResponse:
    return HttpResponse('Archive!!!')


def users(HttpRequest) -> HttpResponse:
    return HttpResponse('users')


def article_number(request, *callback_args, **callback_kwargs):
    my_num = callback_kwargs.get('article_id')
    return render(request, 'article_number.html', {
        'check': my_num % 2,
    })


def article_number_someText(request, *callback_args, **callback_kwargs):
    my_num = callback_kwargs.get('article_id')
    text = callback_kwargs.get('slug_text')
    return render(request, 'article_number.html', {
        'check': my_num % 2,
        'text': text,
    })


def users_number(HttpRequest, user_id) -> HttpResponse:
    return HttpResponse(f'Usrer ID is : {user_id}!!!')


def phone_number(request, *callback_args, **callback_kwargs):
    return HttpResponse("right_phone_number")


def regex(HttpRequest) -> HttpResponse:
    return HttpResponse("My regex!!")



