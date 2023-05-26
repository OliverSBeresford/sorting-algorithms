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

userinput = input("Enter the array you want to sort with each element seperated by spaces:\n").split()
try:
    arr = np.array([float(x) for x in userinput])
except:
    arr = np.array([x for x in userinput], dtype=str)

quicksort(arr, 0, len(userinput) - 1)
print("{", *arr, "}")