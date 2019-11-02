import matplotlib.pyplot as plt
import numpy as np


x = np.random.normal(loc=3, scale=1, size=([10])) + 1.5
y = x/2 + np.random.normal(loc=1.5, scale=0.2,size=[10])
l_x1 = np.linspace(1,8)
l_y1 = l_x1 / 2+0.8
p_x1 = x + (y - (x/2+0.8))*0.4
p_y1 = p_x1 / 2 + 0.8
p_x2 = x - (y - (x*(-2)+3.3))*0.4
p_y2 = p_x2 *(-2) +3.3
l_x2 = np.linspace(-1,1)
l_y2 = l_x2*(-2) + 3.3
plt.plot(l_x1, l_y1, linewidth=3)
plt.plot(l_x2, l_y2, linewidth=3)
plt.xlim([-1,9.5])
plt.ylim([0,6])
plt.scatter(x, y)
plt.scatter(p_x1, p_y1)
plt.scatter(p_x2, p_y2)
plt.show()

