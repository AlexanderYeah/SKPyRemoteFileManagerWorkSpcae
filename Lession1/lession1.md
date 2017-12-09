### 打造一个远程文件管理网站  
* tornado 框架   
Tornado是一种 Web 服务器软件的开源版本。Tornado 和现在的主流 Web 服务器框架（包括大多数 Python 的框架）有着明显的区别：它是非阻塞式服务器，而且速度相当快。  
> pip install tornado  
   
* 1 这就是相当于开启了一个服务器 socket 服务
  ```  
  if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application);
    http_server.listen(8080);
    ioloop.IOLoop.current().start();
  ```  
*  2 系统的路由系统  
*    
```
application = web.Application([
    (r"/",MainPageHandler),
])
```   
* 3 逻辑处理模块 

```  
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # 返回数据
        #self.write("this is alexander");
        # 框架封装好的函数 render 函数直接可以返回html页面
        self.render('index.html');  
        
```