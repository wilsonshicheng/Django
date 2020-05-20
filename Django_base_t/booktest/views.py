from django.shortcuts import render
from django.views import View
from booktest.models import BookInfo,HeroInfo
from django import http
# Create your views here.

# ========增加数据=============
class TestModelView1(View):

    def get(self,request):
        # 1.新增
        # # =======save（）方法新增========
        # book = BookInfo()
        # book.btitle = '西游记'
        # book.bpub_date = '2020-5-20'
        # book.bread = 20
        # book.bcomment = 30
        # # book.is_delete (逻辑删除再新增时，不要进行赋值)
        # # 2.保存数据--将模型对象属性中的值，同步到对应的数据表的字段中。
        # book.save()
        # ===========create方法增加============
        # 语法：模型类.模型关联器.create(模型属性=值)
        # 模型管理器：是由django提供并封装的一个对象，用于调用ORM接口的方法，固定语法
        # BookInfo.objects.create(
        #     btitle='三国演义',
        #     bpub_date = '2020-5-20',
        #     bread = 30,
        #     bcomment = 50,
        # )

        # 2.修改
        # ======save()方法===========
        # 1.查询出要修改的记录/模型对象
        # book = BookInfo.objects.get(id=5)
        # # 2.模型对象属性值修改
        # book.btitle = '西游记后传'
        # # 3.同步到数据库
        # book.save()
        # ==========update方法==========
        # 语法模型类.objects.filter(条件).update(属性=值)
        BookInfo.objects.filter(id=6).update(btitle='西游记')

        return http.HttpResponse('测试增改删')
