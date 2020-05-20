from django.shortcuts import render
from django.views import View
from booktest.models import BookInfo, HeroInfo
from django.db.models import F,Q,Sum,Avg,Max,Min,Count
from django import http


# Create your views here.

# ========增加数据=============
# class TestModelView1(View):
#
#     def get(self, request):
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
        # BookInfo.objects.filter(id=6).update(btitle='西游记')

        # 3.删除
        # 物理删除：
        # BookInfo.objects.filter(id=6).delete()
        # 逻辑删除
        # book = BookInfo.objects.get(id=7)
        # book.is_delete=True
        # book.save()

        # return http.HttpResponse('测试增改删')

    # 4查询

# class TestModelView2(View):
#     def get(self,request):
#        # ======== 基本查询=======
#        # 查询自定的记录：只查询1条数据
#        # 如果只查询一条记录，优先选择get方法【默认只查询1条记录】,如果不存在会爆出DOESTNOTexist异常
#        #  book = BookInfo.objects.get(btitle='射雕英雄传')
#        #  print('删除的记录是：%s'%book.id)
#        #
#        # # 查询所有记录：
#         books = BookInfo.objects.all()
#         for x in books:
#            print(x,type(x))
#
#         # 查询所有记录的个数
#         count = BookInfo.objects.all().count()
#         print(count)
#
#        # 查询满足条件的个数（未被逻辑删除）：
#         count2 = BookInfo.objects.filter(is_delete=False).count()
#         print(count2)
#
#         # 过滤查询
#         book3 = BookInfo.objects.filter(btitle__exact='天龙八部')
#         print(book3)
#         return http.HttpResponse('查询记录测试')

# ===============================复习===================================
class TestModelView3(View):
    def get(self,request):
        # 1.查询书名为天龙八部：
        book = BookInfo.objects.filter(btitle='天龙八部')
        # print(book)
        # 2.查询书名包含湖的书籍：
        books = BookInfo.objects.filter(btitle__icontains='湖')
        # print(books)
        # 3.查询以部结尾的书籍
        books = BookInfo.objects.filter(btitle__endswith='部')
        # print(books)
        # 4.查询书名不为空的书籍：
        books = BookInfo.objects.filter(btitle__isnull=False)
        # print(books)
        # 5.查询编号为1或5的书籍：
        books = BookInfo.objects.filter(id__in=[1,5])
        # print(books)
        # 6.查询编号大于3的书籍：
        books = BookInfo.objects.filter(id__gt=3)
        books2 = BookInfo.objects.filter(id__gte=3)
        book3 = BookInfo.objects.filter(id__lt=3)
        book4 = BookInfo.objects.filter(id__lte=3)
        # print(books)
        # print(books2)
        # print(book3)
        # print(book4)
        # 7.查询id不等于3的书籍：
        book = BookInfo.objects.exclude(id=3)
        # 8.查询1980年发表的书籍：(year,month,day,week,week_day,hour,minute,second)
        book = BookInfo.objects.filter(bpub_date__year=1980)
        # 9.查询1990年1月1日后发表的书籍：
        book = BookInfo.objects.filter(bpub_date__lt='1990-1-1')

# ======================F查询========================
#         10.查询阅读量大于评论量的书籍：
        book = BookInfo.objects.filter(bread__gte=F('bcomment'))
        # 11.查询阅读量大于2倍的评论量的书籍
        book = BookInfo.objects.filter(bread__gt=F('bcomment')*2)


# ========================Q查询========================
#         12.查询阅读量大于20，或者编号小于3的图书：
#         book = BookInfo.objects.filter(Q(bread__gt=20)|Q(id__lt=3))
        book = BookInfo.objects.filter(Q(bread__gt=30)|Q(id__gt=3))
        book = BookInfo.objects.filter(bread__gt=20,id__lt=4)
# ===========================聚合函数查询===============
#         13.统计总阅读量(avg,max,min,sum,min,count)
        res = BookInfo.objects.aggregate(Sum('bread'))
        res = BookInfo.objects.aggregate(Count('id'))

# =========================关联查询==================
#         14.一对多查询：查询编号为1的图书中所有人物信息
        book = BookInfo.objects.get(id=1)
        heros = book.heroinfo_set.all()

        book = BookInfo.objects.get(btitle='天龙八部')
        heros = book.heroinfo_set.all()

        # 15.多对一查询：查询编号为1的英雄出自那本书：
        hero = HeroInfo.objects.get(id=1)
        book = hero.hbook
        hero = HeroInfo.objects.get(hname='乔峰')
        book = hero.hbook
        print(book)

        return http.HttpResponse('练习测试')