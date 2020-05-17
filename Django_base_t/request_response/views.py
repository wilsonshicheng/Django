from django.shortcuts import render
from django.views import View
from django import http
import json


# Create your views here.
# ===========================测试查询字符串==========================
class QSParmView(View):


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

















