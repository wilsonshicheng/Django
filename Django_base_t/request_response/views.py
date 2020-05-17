from django.shortcuts import render
from django.views import View
from django import http


# Create your views here.

class QSParmView(View):
 # 测试查询字符串

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