# 对比python和c运行效率

## 基本思路
分别用python和c编写代码(python调用)对numpy矩阵进行遍历赋值，比较运行时间差异。

## 操作过程
### 编译c代码
~~~ shell
gcc -shared -o init.so init.c
~~~

### 执行测试
输出结果
~~~ text
init with-c time 0.0059635
init python time 0.510822
~~~
结论：使用python代码和c代码速度相差两个数量级。