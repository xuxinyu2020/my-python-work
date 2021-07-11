"""web应用程序的WSGI处理函数"""


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello,web!</h1>']


"""
WSGI对于应用程序有以下标准规定：
1. 应用程序必须是一个可调用的对象。 (function)
2. 应用程序必须接受两个参数并且要按照位置顺序，分别是environ（环境变量），以及start_response函数（负责将响应的status code，headers写进缓冲区，但不返回给客户端）。 
3. 应用程序返回的结果必须是一个可迭代的对象。  (列表)
"""
