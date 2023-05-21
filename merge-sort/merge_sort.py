import numpy as np
import timeit

def merge(array1: np.ndarray, array2: np.ndarray) -> np.ndarray:
  array1Index = array2Index = 0

  lenarray1 = len(array1)
  lenarray2 = len(array2)

  merged = np.empty(lenarray1 + lenarray2, dtype = type(array1[0]))

  while array1Index < lenarray1 and array2Index < lenarray2:
    if array1[array1Index] < array2[array2Index]:
      merged[array1Index + array2Index] = array1[array1Index]
      array1Index += 1
    else:
      merged[array1Index + array2Index] = array2[array2Index]
      array2Index += 1

  if array1Index < lenarray1:
    merged[array1Index + array2Index:] = array1[array1Index:]
  elif array2Index < lenarray2:
    merged[array1Index + array2Index:] = array2[array2Index:]

  return merged

def merge_sort(array1: np.ndarray) -> np.ndarray:
  if len(array1) <= 1:
    return array1

  mid = len(array1) // 2

  left = merge_sort(array1[:mid])
  right = merge_sort(array1[mid:])

  return merge(left, right)

userinput = input("Enter the array you want to sort with each element seperated by spaces:\n").split()

try:
  print("{", *merge_sort(np.array([float(x) for x in userinput])), "}")
except:
  print("{", *merge_sort(np.array([x for x in userinput], dtype=str)), "}")

def wrapper():
    arr = np.array([10, 12, 14, 25, 15, 26, 16, 5])
    merge_sort(arr)

print(timeit.timeit(wrapper))