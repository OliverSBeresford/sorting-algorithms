import numpy as np
import timeit

def quicksort(array: np.ndarray, length) -> np.ndarray:
    if length < 2:
        return array

    indPivot = length -1
    pivot = array[indPivot]

    i = 0
    j = length - 2

    while True:
        while array[i] <= pivot and i < indPivot:
            i += 1
        while array[j] > pivot and j >= 0:
            j -= 1 
        if i < j:
            array[j], array[i] = array[i], array[j]
            i += 1
            j -= 1
        else:
            break
    
    array[indPivot], array[i] = array[i], array[indPivot]

    if i <= 0:
        return quicksort(array[i:], length - i)
    else:
        return np.concatenate((quicksort(array[:i], i), array[i:i+1], quicksort(array[i + 1:], indPivot - i)))

def quicksort_wrapper():
    return quicksort(np.array([10, 9, 2, 1, 3, 2, 5, 1, 4]), 9)

print(quicksort_wrapper())
