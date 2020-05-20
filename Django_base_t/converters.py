# 自定义路由转换器
class MobileConverter:
    # 自定义正则表达式
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

