from django.http import HttpResponse


# Create your views here.
def main(HttpRequest) -> HttpResponse:
    return HttpResponse("Hello BANDITOZ!!!")


def acricles(HttpRequest) -> HttpResponse:
    return HttpResponse("ACRICLES!!!")


def acricles_archive(HttpRequest) -> HttpResponse:
    return HttpResponse('Archive!!!')


def users(HttpRequest) -> HttpResponse:
    return HttpResponse('users')


def article_number(HttpRequest, article_id) -> HttpResponse:
    return HttpResponse(f'Article id is: {article_id}.')


def article_number_someText(HttpRequest, article_id, slug_text='') -> HttpResponse:
    return HttpResponse(
        "Arcticle ID is: {}. {}".format(article_id, "Article name is: {}".format(slug_text)
        if slug_text else "This is unnamed article!!!")
    )


def users_number(HttpRequest, user_id) -> HttpResponse:
    return HttpResponse(f'Usrer ID is : {user_id}!!!')


def regex(HttpRequest) -> HttpResponse:
    return HttpResponse("My regex!!")


def phone_number(request, *callback_args, **callback_kwargs):
    return HttpResponse("right_phone_number")
