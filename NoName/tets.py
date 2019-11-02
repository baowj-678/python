def calculateTotalRotorConfiguration(rotorCount, minRotorValue, maxRotorValue):
    nums = []
    for i in range(minRotorValue, maxRotorValue + 1, 1):
        prime = []
        for j in range(minRotorValue, maxRotorValue + 1, 1):
            if(j // i % 0)