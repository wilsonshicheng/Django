from django.urls import path,re_path
from . import views
urlpatterns = [
    # 查询字符串不是路径，是路径中的参数，所以路由不用匹配字符串
    path('querystring/',views.QSParmView.as_view()),
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
    path('url_param2/<mobile:phone_num>/',views.URLParamView2.as_view())

]