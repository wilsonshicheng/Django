from django.shortcuts import render
from django import http
# Create your views here.

def register(request):
    if request.method=="GET":
        return http.HttpResponse('这是一个注册页面')
    else:
        return http.HttpResponse('这是一个注册逻辑')