import random
import time

# Сортировка пузырьком
def BubbleSort(array):
    
    n = len(array)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Быстрая сортировка
def QuickSort(array):
    
    if len(array) <= 1:
        return array
    else:
        n = random.choice(array)
        left = [elem for elem in array if elem < n]
        middle = [n] * array.count(n)
        right = [elem for elem in array if elem > n]
        return QuickSort(left) + middle + QuickSort(right)

    

array = [random.randint(1, 100) for _ in range(1000000)]

startTime2 = time.time()
sortedArray2 = QuickSort(array)
quickSortTime = time.time() - startTime2
print(f"Time quick sort {quickSortTime}");

startTime1 = time.time()
sortedArray = BubbleSort(array)
sortedArrayTime = time.time() - startTime1
print(f"Time bubble sort {sortedArrayTime}");



