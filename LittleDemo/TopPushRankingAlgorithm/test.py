import scipy.io as sio
from toppush import topPush as topPush
from toppush import topPush as topPushWithC
import numpy as np
import time

if __name__ == '__main__':
    data = sio.loadmat("spambase.mat")
    x = data['Xtr']
    y = data['ytr']
    xte = data['Xte'].toarray()
    ans = data['ans']

    x = np.array(x.toarray())
    y = np.array(y)
    # warm up
    for i in range(10):
        w = topPush(x, y)
    # test toppush
    begin = time.time_ns()
    for i in range(10):
        w = topPush(x, y)
    end = time.time_ns()
    topPushTime = end - begin
    # warm up
    for i in range(10):
        w = topPushWithC(x, y)
    # test toppushWithC
    begin = time.time_ns()
    for i in range(10):
        w = topPushWithC(x, y)
    end = time.time_ns()
    topPushWithCTime = end - begin
    print(f"topPush time: {topPushTime / 1e9} s")
    print(f"topPushWithC time: {topPushWithCTime / 1e9} s")