# TopPush Python Code

本项目是对[《Top Rank Optimization in Linear Time》](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/nips14.pdf) 论文的python代码实现。实现过程参考了官方matlab和c代码，原论文以及代码见[origin](目录)。

## 纯python实现
主体toppush函数以及epne函数都用python实现。

### 代码文件
* toppush.py

### 使用方式
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

## python+C实现
用python实现`toppush`函数，用C实现`epne`函数。

### 代码文件
* epne.c
* toppushWithC.py

### 使用方式
1.编译`epne.c`生成`epne.so`动态链接库文件。
~~~ shell
gcc -shared -o epne.so epne.c
~~~
2.直接调用`toppushWithC.py`中的`topPush`函数即可。
例如：
~~~ python
w = topPush(X, y)
~~~

相关参数以全局变量形式定义：
~~~ python
# load C func epne
mylib = cdll.LoadLibrary('epne.so')
epne = mylib.epne

# params
lambdaa = 1  # radius of l2 ball
maxIter = 10000  # maximal number of iterations
tol = 1e-4  # the relative gap
debug = False  # the flag whether it is for debugging
delta = 1e-6
~~~

## 实验对比
### 代码文件
* test.py

### 实验结果
~~~ text
topPush time: 19.8399107 s
topPushWithC time: 17.9153129 s
~~~

### 经验教训
numpy.ndarray运算后会生成新的numpy.ndarray，不是在原数据上进行修改。例如（data = -data，会生成新的数据）