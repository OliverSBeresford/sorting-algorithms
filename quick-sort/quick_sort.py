import numpy as np

def quicksort(array: np.ndarray, length) -> np.ndarray:
    if length < 2:
        return array

    pivot = array[length - 1]

    i = 0
    j = length - 2

    while True:
        while array[i] <= pivot:
            i += 1
        while array[j] > pivot:
            j -= 1 
        if i < j:
            array[j], array[i] = array[i], array[j]
            i += 1
            j -= 1
        else:
            break
    
    array[length - 1], array[i] = array[i], array[length - 1]

    return array

print(quicksort(np.array([5, 2, 1, 1.5, 6, 4, 2]), 7))