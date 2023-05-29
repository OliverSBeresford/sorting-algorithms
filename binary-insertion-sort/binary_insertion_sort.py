import numpy as np

def binary_insertion_sort(array: np.ndarray, length) -> np.ndarray:
    current_index = 1

    while current_index < length:
        num = array[current_index]
        left = 0
        right = current_index - 1

        while left <= right:
            mid = (left + right) // 2

            if array[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        
        # left is the correct location for temp
        array[left+1:current_index+1] = array[left:current_index]
        array[left] = num

        current_index += 1
    
    return array

userinput = input("Enter the array you want to sort with each element seperated by spaces:\n").split()

try:
  print("{", *binary_insertion_sort(np.array([float(x) for x in userinput]), len(userinput)), "}")
except:
  print("{", *binary_insertion_sort(np.array([x for x in userinput], dtype=str), len(userinput)), "}")