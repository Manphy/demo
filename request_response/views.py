from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def weather(request,city,year):
    print('city=%s' % city)
    print('year=%s' % year)
    return HttpResponse('OK')


def weather2(request,year,city):
    print('city=%s' % city)
    print('year=%s' % year)
    return HttpResponse('weather2')