import numpy as np

def partition(array: np.ndarray, start: int, end: int) -> int:
    pivot = array[end]

    i = start - 1
    j = end

    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while j and array[j] > pivot:
            j -= 1

        if i >= j:
            array[i], array[end] = array[end], array[i]
            return j
        
        array[i], array[j] = array[j], array[i]

def quicksort(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        quicksort(array, start, pivot_index)
        quicksort(array, pivot_index + 1, end)

arr = np.array([10, 12, 14, 25, 15, 26, 16, 5])
startIndex = 0
endIndex = len(arr) - 1
quicksort(arr, startIndex, endIndex)
print(arr)