# TopPush Python Code

本项目是对[《Top Rank Optimization in Linear Time》](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/nips14.pdf) 论文的python代码实现。实现过程参考了官方matlab和c代码，原论文以及代码见[origin](目录)。

## 使用方式
直接调用`toppush.py`中的`topPush`函数即可。
例如：
~~~ python
w = topPush(X, y)
~~~

相关参数以全局变量形式定义：
~~~ python
lambdaa = 1  # radius of l2 ball
maxIter = 10000  # maximal number of iterations
tol = 1e-4  # the relative gap
debug = False  # the flag whether it is for debugging
delta = 1e-6
~~~


### 经验教训
numpy.ndarray运算后会生成新的numpy.ndarray，不是在原数据上进行修改。例如（data = -data，会生成新的数据）