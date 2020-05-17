from django.shortcuts import render
from django import http
from django.views import View
# Create your views here.
# ===================定义函数视图====================
# def register(request):
#     if request.method=="GET":
#         return http.HttpResponse('这是一个注册页面')
#     else:
#         return http.HttpResponse('这是一个注册逻辑')

# ===================定义类视图====================

class RegisterView(View):
    def get(self,request):
        return http.HttpResponse('这是一个注册页面')
    def post(self,request):
        return http.HttpResponse('这是一个注册逻辑')

class LoginView(View):
    def get(self, request):
        return http.HttpResponse('这是一个登录页面')

    def post(self, request):
        return http.HttpResponse('这是一个登录逻辑')
