import numpy as np

def insertion_sort(array: np.ndarray) -> np.ndarray:
    for i in range(len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value
    return array

userinput = input("Enter the array you want to sort with each element seperated by spaces:\n").split()

try:
  print("{", *insertion_sort(np.array([float(x) for x in userinput])), "}")
except:
  print("{", *insertion_sort(np.array([x for x in userinput], dtype=str)), "}")