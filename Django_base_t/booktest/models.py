from django.db import models

# Create your models here.

class BookInfo(models.Model):

    # 定义模型类属性，映射数据表字段
    # 字段有哪些，属性就有哪些，其中，默认的id主键不需要设置。
    # 字段类型是什么，属性就指定对应的类型
    # 字段约束条件，属性对应的约束条件就是什么
    btitle = models.CharField(max_length=64)
    bpub_date = models.DateTimeField(verbose_name='发布日期')
    bread = models.IntegerField(default=0,verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')
    # 数据表的删除：
        # 1.逻辑删除：设计一个bool字段，标记该记录是否需要操作 。
        # 2.物理删除：从磁盘上删除该记录。

    # 自定义数据表的表名:
    class Meta:
        # Django封装好的模型类的元类，模型类的底层配置类
        db_table = "tb_bookinfo"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle  # 输出该模型数据对象时，只输出书名



class HeroInfo(models.Model):
    """英雄信息：演示一对多，多方"""
    # 确定性别字段的取值范围
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='英雄属于的图书')
    hname = models.CharField(max_length=20, verbose_name='人名')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'

    def __str__(self):
        return self.hname