from django.shortcuts import render
from django.http import HttpResponse
from sign_up.models import *


def platform(request):
    return render(request, 'platform.html')


def webinar_sign_up(request):
    first_name, last_name, email, genre = parse_request(request)

    user = OpsUser.objects.filter(email=email, genre=genre).first()
    if user:
        if user.first_name == first_name and user.last_name == last_name:
            return HttpResponse('You are already registered!', 200)        
        else:
            return HttpResponse('The email is already used!', status=405)
    else:
        OpsUser.objects.create(first_name=first_name, last_name=last_name, genre=genre, email=email)
        return HttpResponse('We have sent an e-mail to you for verification. Follow the link provided to finalize the signup process. Please contact us if you do not receive it within a few minutes.', 201)


def parse_request(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    genre = request.GET.get('genre')

    return first_name, last_name, email, genre
