#coding=utf-8;

# 导入tornado

from tornado import web,ioloop,httpserver
import os

"""
    逻辑处理模块
"""
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # 返回数据
        #self.write("this is alexander");
        # mac 系统的路径'/'
        disk = [];
        temp = {
            'path':'/',
            'is_path':True,
            'name':'/',
            'time':'',
            'type':'根目录'

        }
        disk.append(temp);
        # 框架封装好的函数 render 函数直接可以返回html页面
        # 将参数传递至HTML 页面中 用户数据的展示
        self.render('index.html',disk=disk);

"""
    路由系统

    /index 相当于url，在浏览器就要输入
"""
application = web.Application([
    (r"/",MainPageHandler),

])
"""
    socket 服务 处理请求的。
    相当于一个公司的前台
"""
if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application);
    http_server.listen(8080);
    ioloop.IOLoop.current().start();