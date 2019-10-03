from matplotlib import pyplot as plt

plt.scatter([3, 5, 4], [5, 3, 5.5], color='c', marker='o')
plt.scatter([5, 6, 4.5], [5, 6, 4], color='c', marker='+', s=90)
plt.plot([1,9],[9,1],color='b', linestyle=':')
plt.plot([2, 6], [6, 2],color='b', linestyle=':')
plt.plot([2, 7], [7, 2],color='r', linestyle='-')
plt.xlim([2, 7])
plt.ylim([2, 7])
plt.show()