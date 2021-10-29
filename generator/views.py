from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def genPassword(request):
    length = int(request.GET.get('length'))
    if length < 8:
        return render(request, 'password.html', {'invalid':'Password length must be at least 8 chars'})
    chars = list('abcdefghijklmnopqrstuxyz')
    generated_pass = ""

    if request.GET.get('uppercase') == 'on':
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYZ'))
    if request.GET.get('special') == 'on':
        chars.extend(list('$%&/(#!{*-_=}()<,>'))
    if request.GET.get('numbers') == 'on':
        chars.extend(list('0123456789'))

    for c in range(length):

        generated_pass += choice(chars)

    return render(request, 'password.html', {'password': generated_pass})
