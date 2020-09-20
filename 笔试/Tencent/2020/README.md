# 腾讯2020秋季笔试题

## 第一轮

### 第一题：

<img src="T1-1-1.jpg" alt="pic1" style="zoom:50%;" />

<img src="T1-1-2.jpg" alt="pic2" style="zoom:50%;" />

<img src="T1-1-3.jpg" alt="pic3" style="zoom:50%;" />

[code](T1-1.py)



***

### 第二题：

<img src="T1-1-1.jpg" alt="pic1" style="zoom:50%;" />

<img src="T1-2-2.jpg" alt="pic2" style="zoom:50%;" />

[code](T1-2.py)



***

### 第三题：

<img src="T1-3-1.png" alt="pic1" style="zoom:50%;" />

<img src="T1-3-2.jpg" alt="pic2" style="zoom:50%;" />

[code](T1-3.py)



***

### 第四题：

<img src="T1-4-1.png" alt="pic1" style="zoom:50%;" />

<img src="T1-4-2.jpg" alt="pic2" style="zoom:50%;" />

<img src="T1-4-3.jpg" alt="pic3" style="zoom:50%;" />

[code](T1-4.py)



***

### 第五题：

<img src="T1-5-1.png" alt="pic1" style="zoom:50%;" />

<img src="T1-5-2.jpg" alt="pic2" style="zoom:50%;" />

[code](T1-5.py)

## 第二轮

### 第一题：

<img src="T2-1-1.png" alt="picture1" style="zoom:50%;" />

<img src="T2-1-2.png" alt="picture1" style="zoom:50%;" />

[code](T2-1.py)



****

### 第二题：

<img src="T2-2-1.png" alt="picture1" style="zoom:50%;" />

<img src="T2-2-2.png" alt="picture2" style="zoom:50%;" />

[code](T2-2.py)



***

### 第三题：

<img src="T2-3-1.png" alt="pic1" style="zoom:50%;" />

<img src="T2-3-2.png" alt="pic2" style="zoom:50%;" />

[code](T2-3.py)

**解析**：

**令**

$f(x)$：表示长度为$x$的巧克力棒到长度小于$d$的次数；

$\phi(i,x)=\frac{1}{x}$：表示长度为$x$的巧克力棒，在$i$点扳断的概率；

**则**：

$$f(x)=\left\{\begin{aligned} 0\qquad x\leq d \\ 1+\int_0^df(t)\phi(t)dt + \int_d^xf(t)\phi(t)dt \quad x > d \end{aligned}\right.$$

$$=\left\{\begin{aligned} 0\quad x\leq d \\ 1 + \int_d^xf(t)\phi(t)dt \quad x > d \end{aligned}\right.$$

$$=\left\{\begin{aligned} 0\quad x\leq d \\ 1 + (\int_d^xf(t)dt)/x \quad x > d \end{aligned}\right.$$

**解得**：

$$f(x)=\left\{\begin{aligned} 0\qquad x\leq d \\ 1+\ln{\frac{x}{d}} \quad x>d\end{aligned}\right.$$

***

### 第四题：

<img src="T2-4-1.png" alt="pic1" style="zoom:50%;" />

<img src="T2-4-2.png" alt="pic2" style="zoom:50%;" />

[code](T2-4.py)



***

### 第五题：

<img src="T2-5-1.png" alt="pic1" style="zoom:50%;" />

<img src="T2-5-2.png" alt="pic2" style="zoom:50%;" />

[code](T2-5.py)

