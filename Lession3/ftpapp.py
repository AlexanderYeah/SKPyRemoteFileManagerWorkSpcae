#coding=utf-8;

# 导入tornado

from tornado import web,ioloop,httpserver
import os
import time

"""
    逻辑处理模块
"""
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # 返回数据
        #self.write("this is alexander");
        # mac 系统的路径'/'
        disk = [];

        # 判断是否第一次get 请求，参数是否带有path
        path = self.get_argument('path',default=None);
        print(path);
        if path:
            # 证明不是第一次请求
            # 列出根路径下面的所有的文件夹
            print(path);
            dir_list = os.listdir(path);
            print(dir_list);
            # 把list 下的路径再次放进去
            for item in dir_list:
                temp_path =  os.path.join(path,item);
                temp = {
                    'path':temp_path,
                    # 分辨是文件还是路径
                    'name':item,
                    #获取文件的修改时间
                    'time':time.strftime("%Y/%m/%d %H:%M",time.localtime(os.path.getctime(temp_path))),

                }
                # 判断是否路径 还是文件
                if os.path.isfile(temp_path):
                    temp['is_path'] = False;
                    temp['type'] = '文件';
                else:
                    temp['is_path'] = True;
                    temp['type'] = '文件夹';

                # 放进disk 中
                disk.append(temp);

        else:
            temp = {
                'path': '/Users/alexander/Desktop',
                'is_path': True,
                'name': '/Users/alexander/Desktop',
                'time': 'none',
                'type': '根目录'

            }
            disk.append(temp);
        # 框架封装好的函数 render 函数直接可以返回html页面
        # 将参数传递至HTML 页面中 用户数据的展示
        self.render('index.html',disk=disk);


# 下载模块
class DownLoadHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        path = self.get_argument('path',default=None);
        print("download/path-%s", path);
        if path:

            with open(path,'rb') as f:
                # 不停的读取指定的文件，一直读取完毕 进行返回
                while True:
                    data = f.read(1024);
                    if data:
                        self.write(data);
                    else:
                        break;


# 删除模块 处理逻辑就是获取路径 ，判断是否是一个文件，是的话，可以删除，不是的话，提醒用户，不让删除
class DeleteHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        path = self.get_argument('path',default=None);
        if path:
            if os.path.exists(path):
                if os.path.isfile(path):
                    # 获取当前文件的父路径，以便于 删除文件之后的重定向
                    parrent_path = os.path.dirname(path);

                    if os.path.isdir(path):
                        os.removedirs(path);
                    else:
                        os.remove(path);
                    # redirect 重定向
                    self.redirect('/index?path=%s' % parrent_path);
                else:
                    self.write("不要直接删除文件夹");
        else:
            self.write("文件不存在");



"""
    路由系统

    /index 相当于url，在浏览器就要输入
"""
application = web.Application([
    # 首页的话 跳转首页操作
    (r"/index",MainPageHandler),
    # 下载的话 进行下载操作
    (r"/download",DownLoadHandler),
    # 删除操作
    (r"/delete",DeleteHandler),

])
"""
    socket 服务 处理请求的。
    相当于一个公司的前台
"""
if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application);
    http_server.listen(8080);
    ioloop.IOLoop.current().start();