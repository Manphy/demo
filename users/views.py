from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
"""
1视图至少要一个参数用于request请求，
用于接收django构造的包含了请求数据的HttpRequest对象，
通常命名为request
2视图函数必须要有响应对象，可以将要返回的数据放到HttpResponse对象中。
"""

def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    ：return :响应对象
    """
    return HttpResponse("hello world")

def say(request):
    return HttpResponse('say')

def say_hello(request):
    return HttpResponse('say_hello')


