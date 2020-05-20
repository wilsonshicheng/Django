from django.urls import path ,re_path
from . import views
# from django.views import url

urlpatterns =[
    path('users/register/',views.RegisterView.as_view()),
    # 使用re_path编写路由
    re_path(r'^users/login/$',views.LoginView.as_view())

]
