from django.urls import path
from . import views
urlpatterns = [
    # 查询字符串不是路径，是路径中的参数，所以路由不用匹配字符串
    path('querystring/',views.QSParmView.as_view()),
    path('formdata/',views.FormDataParamView.as_view()),
    path('json/',views.JSONParamView.as_view()),

]