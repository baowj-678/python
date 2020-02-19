import numpy as np


def InsertSort(array):
    for i in range(1, array.shape[0], 1):
        key = array[i]
        j = i - 1
        while(j >= 0 and array[j] > key):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


def main():
    # array = [1, 2, 3, 4]
    # array = np.array(array)
    array = np.random.randn(1000)
    print('first:', array)
    array = InsertSort(array)

    print('after:', array)


main()
