import numpy as np

def bubble_sort(array: np.ndarray, end: int) -> None:
    if not end:
        return
    
    index1 = 0
    index2 = 1

    while index2 <= end:
        if array[index1] > array[index2]:
            array[index1], array[index2] = array[index2], array[index1]
        index2 += 1
        index1 += 1
    
    bubble_sort(array, end - 1)

userinput = input("Enter the array you want to sort with each element seperated by spaces:\n").split()
try:
    arr = np.array([float(x) for x in userinput])
except:
    arr = np.array([x for x in userinput], dtype=str)

bubble_sort(arr, len(userinput) - 1)
print("{", *arr, "}")