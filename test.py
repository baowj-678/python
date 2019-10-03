from matplotlib import pyplot as plt
import numpy as np

data = np.array([])
num = 200
for i in range(num):
    p = []
    x = np.random.uniform(0, 6)
    y = np.random.uniform(-5, 2)
    if y < ((7 - x * x) / 6):
        p.append(x)
        p.append(y + np.random.uniform(0, 0.7))
        p.append(-1)
    elif y > ((7 - x * x) / 6):
        p.append(x)
        p.append(y + np.random.uniform(-0.7, 0))
        p.append(1)
    data = np.append(data, p)
data = data.reshape([-1, 3])
print(data.shape)
data_index = data[:, 2]
data_plus = data[data_index == 1]
data_minus = data[data_index == -1]
plt.scatter(data_plus[:, 0],data_plus[:,1])
plt.scatter(data_minus[:, 0],data_minus[:,1])
plt.show()