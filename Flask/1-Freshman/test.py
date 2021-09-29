from scipy import integrate
import matplotlib.pyplot as plt
import math

d = 0

def func(x):
    global d
    return math.cos(d/math.pow(10000, x))

if __name__ == '__main__':
    x = []
    y = []
    z = []
    for i in range(1, 1000, 1):
        d = i
        x.append(i)
        y.append(integrate.quad(func, 0., 1.)[0])
        z.append(func(0.1))
    plt.plot(x, y)
    # plt.plot(x, z)
    # print(y)
    plt.show()

