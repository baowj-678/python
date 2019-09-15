from matplotlib import pyplot as plt
import numpy as np

a = np.array([[5, 5]
    ,[6, 6]
    ,[3, 5]
    ,[5, 3]

])

plt.scatter(a[:2, 0], a[:2, 1],color='y', marker='+', s=100)
plt.scatter(a[2:,0], a[2:, 1],color='y', marker='o')
plt.plot([2,6],[6,2],color='b', linestyle=':')
plt.plot([1,9],[9,1],color='b', linestyle=':')
plt.plot([2,7],[7, 2],color='r', linestyle='-')
# plt.plot([3,5.5],[10,2],color='c', linestyle='-')
plt.xlim(2, 7)
plt.ylim(2, 7)
plt.xlabel('X1', fontsize=12)
plt.ylabel('X2', fontsize=12)
plt.show()
