import time
import numpy as np
from ctypes import cdll, c_void_p


mylib = cdll.LoadLibrary('init.so')
init = mylib.init


def init_matrix_with_c(mat: np.ndarray, row: int, col: int):
    init(c_void_p(mat.ctypes.data), row, col)
    return mat


def init_matrix(mat: np.ndarray, row: int, col: int):
    for i in range(row):
        for j in range(col):
            mat[i, j] = i + j + 2
    return mat


if __name__ == '__main__':
    # get matrix
    row, col = 100, 234
    mat = np.zeros([row, col])
    # warm up
    for i in range(100):
        init(c_void_p(mat.ctypes.data), row, col)
    # test with-c
    begin = time.time_ns()
    for i in range(100):
        init(c_void_p(mat.ctypes.data), row, col)
    end = time.time_ns()
    print('init with-c time {}'.format((end - begin) / 1e9))
    # warm up
    for k in range(100):
        for i in range(row):
            for j in range(col):
                mat[i, j] = i + j + 2
    # test python
    begin = time.time_ns()
    for k in range(100):
        for i in range(row):
            for j in range(col):
                mat[i, j] = i + j + 2
    end = time.time_ns()
    print('init python time {}'.format((end - begin) / 1e9))
