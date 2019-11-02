from mpl_toolkits import mplot3d
# matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

# ax = plt.axes(projection='3d')

#三维线的数据
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, 'gray')

# 三维散点的数据
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
zdata = np.ones([100])# + np.random.normal(0, 0.03, size=[100])
# ax.axis([-2,2,0.5,1.5])
# ax.scatter3D(xdata, zdata, ydata, cmap='Greys')
plt.scatter(xdata, ydata)
plt.show()