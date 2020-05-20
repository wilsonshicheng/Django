from django.urls import path,re_path
from . import views
urlpatterns = [
    # 查询字符串不是路径，是路径中的参数，所以路由不用匹配字符串
    path('querystring/',views.QSParamView.as_view()),
    path('formdata/',views.FormDataParamView.as_view()),
    path('json/',views.JSONParamView.as_view()),
    # path('url_param1/<路由转换器【提取路径参数】:变量【接受提取的路径参数】>/', views.URLParamView.as_view()),
    # 这里的int可以替换成下面
    #     DEFAULT_CONVERTERS = {
    #         'int': IntConverter(),匹配正整数
    #         'path': PathConverter(),匹配任何非空字符串，包含了路径分隔符
    #         'slug': SlugConverter(),匹配字母、数字及横岗、下划线组成的字符串
    #         'str': StringConverter(),匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
    #         'uuid': UUIDConverter(),匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00
    #     }

    path('url_param1/<str:number>/', views.URLParamView.as_view()),
    path('url_param2/<mobile:phone_num>/',views.URLParamView2.as_view()),
    # re_path(r'^url_param3/18500001111/$',views.URLParamView3.as_view()),
   # re_path提取手机号码步骤：
    # 1.先用正则匹配手机号
    # re_path(r'^url_param3/1[3-9]\d{9}/$',views.URLParamView3.as_view())
    # 2.如果正则匹配成功，就是用正则的组把手机号码提取出来
    # re_path(r'^url_param3/(1[3-9]\d{9})/$',views.URLParamView3.as_view())
    # 3.需要在正则的组中定义一个变量，把提取的手机号码保存起来。
    re_path(r'^url_param3/(?P<mobile_number>1[3-9]\d{9})/$', views.URLParamView3.as_view()),

    # ****使用url方式
    # url(r'^url_param3/(?P<mobile_number>1[3-9]\d{9})/$', views.URLParamView3.as_view())
    path('response1/', views.Response1View.as_view()),
    path('resp_json/', views.JsonResponseView.as_view()),

    # *****重定向 ,给子路由添加别名path（"","",name=")
    path('index/', views.IndexView.as_view(),name='index'),
    path('login_redirect/', views.IndexView.as_view()),
]

# path 和 re_path选择：
# 如果希望自己编写所有的正则表达式，选择re_path()
# 其他都是path（）