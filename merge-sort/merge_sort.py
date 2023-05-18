import numpy as np

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

print("Merging [1, 6, 8] and [2, 4, 7]:\n", merge(np.array([1, 6, 8]), np.array([2, 4, 7])))