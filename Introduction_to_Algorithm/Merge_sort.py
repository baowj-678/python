import numpy as np


class MergeSort():
    def __init__(self, array):
        self.array = array
        self.space = np.zeros(array.shape[0])

    def Mergesort(self):
        return self.MergesortInner(0, self.array.shape[0] - 1)

    def MergesortInner(self, left, right):
        if(left == right):
            return
        mid = (left + right) // 2
        self.MergesortInner(left, mid)
        self.MergesortInner(mid + 1, right)
        self.Merge(left, mid, right)
        return self.array

    def Merge(self, left, mid, right):
        le = left
        r = mid + 1
        a = left
        while(le <= mid and r <= right):
            if(self.array[le] > self.array[r]):
                self.space[a] = self.array[r]
                r = r + 1
            else:
                self.space[a] = self.array[le]
                le = le + 1
            a = a + 1
        while(le <= mid):
            self.space[a] = self.array[le]
            a = a + 1
            le = le + 1
        while(r <= right):
            self.space[a] = self.array[r]
            a = a + 1
            r = r + 1
        for i in range(left, right + 1, 1):
            self.array[i] = self.space[i]
        return


def main():
    array = np.random.randn(400)
    merge = MergeSort(array)
    print(merge.Mergesort())
    pass


main()
