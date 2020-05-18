from django.utils.deprecation import MiddlewareMixin

# 自定义中间件：
# 1.它是标准的python类
# 2.继承自MiddlewareMixin
# 3.可以定义中间件方法中的一个或者多个，方法名字不可以乱写。

class TestMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        """处理请求前自动调用"""
        print('process_request1 被调用')

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 处理视图前自动调用
        print('process_view1 被调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('process_response1 被调用')
        return response

# 创建多个自定义中间件，复制粘贴就好。

class TestMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        """处理请求前自动调用"""
        print('process_request1 被调用')

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 处理视图前自动调用
        print('process_view1 被调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('process_response1 被调用')
        return response

#中间件的执行流程：
# 请求：从上往下
# 响应：从下往上