# Flask入门





### Error

1. **This is a development server. Do not use it in a production deployment.**

    ![image-20210404190250044](.md\image-20210404190250044.png)

**解决方法**：

在文件假如下面语句：

~~~python
from wsgiref.simple_server import make_server
server = make_server('127.0.0.1', 5000, app)
server.serve_forever()
~~~

