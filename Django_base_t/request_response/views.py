from django.shortcuts import render ,redirect,reverse
from django.views import View
from django import http
import json


# Create your views here.
# ===========================测试查询字符串==========================
class QSParamView(View):


    def get(self,request):
        # request.GET:专门用于提取请求地址中的查询字符串参数
        # 注意点：在提取查询字符串参数时，跟请求方式没有任何的关系，即任何请求方式，只要传递了查询字符串，--
        # --都是使用request.GET
        # query_str_parm = request.GET
        # name = query_str_parm.get('name')
        name = request.GET.get('name')
        age = request.GET.get('age')
        print(name,age)

        return http.HttpResponse('GET测试提取字符串')


    def post(self, request):
        name = request.GET.get('name')
        age = request.GET.get('age')
        print(name, age)

        return http.HttpResponse('POST测试提取字符串')

# ===========================测试查询请求体==========================

# 1.查询表单数据
class FormDataParamView(View):
    # POST http://127.0.0.1/8000/formdata/
    def post(self,request):
        # 方式：request.POST.
        # form_data = request.POST
        # username = form_data.get('username')
        # password = form_data.get('password')

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        return http.HttpResponse('测试提取表单类型的请求体数据')


# 2.查询Jason数据
# 非表单类型的请求体数据有很多种：jason、xml。。。
# 由于类型种类很多，Django不想知道当前是哪一种。如果需要区分比较复杂，所以django没有添加解析功能。
# 解决方案：Django提供了了一个属性，用于接收非表单类型的请求体数据。，提取数据后，自行处理。
class JSONParamView(View):
    # POST http://127.0.0.1/8000/jason/
    def post(self,request):

        # 先获取非表单类型的请求体数据：方式：request.body
        origin_data = request.body
        # json的loads方法：讲原始的json数据转成字典
        json_dict = json.loads(origin_data)
        username = json_dict.get('username')
        password = json_dict.get('password')
        print(username,password)

        return http.HttpResponse('测试提取表单类型的请求体数据:JSON')

# ===========================测试查询URL特定数据==========================
# 需求1：http://127.0.0.1:8000/url_param1/18/
# 提取路径中的数字18
# 需求2：http://127.0.0.1:8000/url_param2/18500001111/
# 提取路径中的手机号18500001111


# 1.path()提取路径参数
class URLParamView(View):
    # 使用path提取普通参数路径
    # 提取路径参数是在路由系统里面完成的，因为路径再路由系统进行处理。
    def get(self,request,number):
        # 接受路径参数number
        # 注意点：视图内部的关键字参数必须和路由中的关键字一样。
        print(number)
        return http.HttpResponse('测试path（）提取普通参数路径')

class URLParamView2(View):
    # 使用path提取普通参数路径
    # 提取路径参数是在路由系统里面完成的，因为路径再路由系统进行处理。
    def get(self,request,phone_num):
        # 接受路径参数number
        # 注意点：视图内部的关键字参数必须和路由中的关键字一样。
        print('提取的手机号码是：',phone_num)
        return http.HttpResponse('测试path提取电话号码')

# 2.re_path()提取路径参数
# 需求2：http://127.0.0.1:8000/url_param3/18500001111/
# 提取路径中的手机号18500001111


class URLParamView3(View):
    # 使用re_path提取普通参数路径
    # 提取路径参数是在路由系统里面完成的，因为路径再路由系统进行处理。
    def get(self,request,mobile_number):
        # 接受路径参数number
        # 注意点：视图内部的关键字参数必须和路由中的关键字一样。
        print('提取的手机号码是：',mobile_number)
        return http.HttpResponse('测试re_path提取电话号码')

# ===========================响应数据==========================
# 1.HttpReponse()响应数据

class Response1View(View):

    def get(self,request):
        # 需求：http://127.0.0.1:8000/response1/
        # return http.HttpResponse(content='响应体',content_type='数据类型 默认text/html',status='状态码，默认：200')
        # 原始状态
        # return http.HttpResponse(content='演示HttpResponse', content_type='text/html', status=200)
        # 简化1
        # return http.HttpResponse(content='演示HttpResponse')
        # 简化2
        return http.HttpResponse('演示HttpResponse')

# 提示：默认的情况HttpResoponse响应html字符串的，如果需要响应html字符串以外的数据，如何实现？
#         1.HttpResponse(响应体：图片的原始数据，content_type='image/jpg')



# 2.JsonResponse()响应JSON数据
# 需求：get:http://127.0.0.1:8000/resp_json/
# class JsonResponseView(View):
#     def get(self,response):
#         dict_data = {
#             'name':'wilson',
#             'age':18
#         }
#         return http.JsonResponse(dict_data)

# 扩展：JsonResponse出了默认接受字典意外，时候可以接受其他数据类型
# return http.JsonResponse('列表数据',safe=False)

class JsonResponseView(View):
    def get(self,response):
        list_data = ['1','2','3']
        return http.JsonResponse(list_data,safe=False)


# 3.redirect()响应重定向数据
# 需求：
# 准备一个用于处理用户登录类视图LoginRedirectView
# 访问LoginRedirectView时，如果其中的登录逻辑处理完成，我们将用户重定向到首页

class IndexView(View):
    # 需求：get:http://127.0.0.1:8000/index/
    def get(self,request):
        return http.HttpResponse('网站首页')


class LoginRedirectView(View):
    # 需求：post:http://127.0.0.1:8000/login_redirect/
    def post(self,request):
        # 1.处理登录逻辑
        # 2.如果用户登录成功，将用户引导到首页（重定向）
        # return redirect('/index/') --利用reverse解决路由变化的问题
    # 或者 return redirect('http://127.0.0.1:8000/index/')
    # 注意点：重定向的网址需要加根路径：index/-----→/index/

# 问题：
#     一旦路由发生变化，那么使用该路由的所有源代码都需要变。
# 解决方案：
#     路由的反向解析reverse（）
#     原理：可以动态根据路由的别名，去解析真实的地址
#     方式：return redirect(reverse('总路由的别名：子路由的别名'))
        return redirect(reverse('requeset_response:index'))
