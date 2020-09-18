def meanderingArray(unsorted):
    tmp = sorted(unsorted)
    a = 0
    i = 0
    while i < len(unsorted):
        unsorted[i] = tmp[len(tmp) - 1 - a]
        i += 1
        if i < len(unsorted):
            unsorted[i] = tmp[a]
            i += 1
            a += 1
    return unsorted


if __name__ == "__main__":
    num = [-1, 1, 2, 3, -5]
    print(meanderingArray(num))
