import numpy as np

def insertion_sort(array: np.array) -> np.array:
    for i in range(len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value
    return array

print(insertion_sort(np.array([int(x) for x in input("Enter the list, numbers separated by spaces:\n").split()])))