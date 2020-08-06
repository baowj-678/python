def random_select(numbers, k):
    if len(numbers) == 1 and k == 1:
        return numbers[0]
    # devide
    mid_value = partition(numbers)
    mid = len(numbers) - 2
    left = 1
    right = len(numbers) - 3
    if(len(numbers) > 3):
        while left < right:
            while numbers[left] < mid_value:
                left = left + 1
            while right > 0 and numbers[right] >= mid_value:
                right = right - 1
            if left < right:
                temp = numbers[left]
                numbers[left] = numbers[right]
                numbers[right] = temp
        temp = numbers[mid]
        numbers[mid] = numbers[left]
        numbers[left] = temp
        mid = left
    else:
        right = len(numbers)
        for left in range(right):
            for mid in range(left + 1, right):
                if(numbers[left] > numbers[mid]):
                    temp = numbers[left]
                    numbers[left] = numbers[mid]
                    numbers[mid] = temp
        mid = (right - 1)//2

    # conquer
    if mid < k - 1:
        return(random_select(numbers[mid + 1:], k - 1 - mid))
    elif mid > k - 1:
        return(random_select(numbers[:mid], k))
    else:
        return numbers[mid]


def partition(numbers):
    if len(numbers) < 2:
        return 0
    else:
        first = 0
        last = len(numbers) - 1
        mid = (first + last)//2
        if(numbers[last] < numbers[first]):
            temp = numbers[last]
            numbers[last] = numbers[first]
            numbers[first] = temp
        if(numbers[last] < numbers[mid]):
            temp = numbers[mid]
            numbers[mid] = numbers[last]
            numbers[last] = numbers[mid]
        if(numbers[mid] < numbers[first]):
            temp = numbers[mid]
            numbers[mid] = numbers[first]
            numbers[first] = numbers[mid]
        temp = numbers[mid]
        numbers[mid] = numbers[last - 1]
        numbers[last - 1] = temp
        return numbers[last - 1]


def main():
    numbers = input('input the numbers\n')
    numbers = numbers.split()
    numbers = [int(num) for num in numbers]
    k = eval(input('input the k\n'))
    print(random_select(numbers, k))


main()
