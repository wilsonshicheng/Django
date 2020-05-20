"""Django_base_t URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
# 导入注册路由器的转换方法
from django.urls.converters import register_converter
from converters import MobileConverter
# register_converter('自定义的路由转换器的类','别名')
register_converter(MobileConverter,'mobile')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    # 给路由起别名include("",namespace=")
    path('',include(('request_response.urls','request_response'),namespace='request_response')),#缺少app_name参数
    # 注意点：如果定义了总路由的namespace，一定要记得定义app_name
    path('',include('booktest.urls')),

]


