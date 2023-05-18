# Sorting Algorithms

This repository contains implementations of various sorting algorithms in Python and C++.

## Usage

- **Python**:
  - Open the desired sorting algorithm file (e.g., `merge_sort.py`).
  - Copy the entire code.
  - Paste it into your Python file or interactive Python environment.
  - Call the sorting function by its name (the same name as the file and algorithm) with a list of elements to be sorted. (For now, the algorithm only works with numpy arrays. Lists coming soon.)
    ```python
    sorted_arr = merge_sort(arr)
    ```
  - Customize the code or modify the input list (`arr`) to suit your needs.

- **C++**:
  - Open the desired sorting algorithm file (e.g., `merge_sort.cpp`).
  - Copy the entire code.
  - Paste it into your C++ source file or create a new C++ file.
  - Call the sorting function by its name (the same name as the file and algorithm) with an array or vector of elements to be sorted.
    ```cpp
    int sortedArr[] = mergeSort(arr);
    ```
  - Customize the code or modify the input array (`arr`) to suit your needs. (Same here, only works with arrays, but soon I'll add the functionatlity with vectors.)

## Algorithms

- [merge_sort.py](merge_sort.py): Implementation of the Merge Sort algorithm in Python.
  - For more information, see the [Merge Sort Wikipedia article](https://en.wikipedia.org/wiki/Merge_sort).

- [insertion_sort.py](insertion_sort.py): Implementation of the Insertion Sort algorithm in Python.
  - For more information, see the [Insertion Sort Wikipedia article](https://en.wikipedia.org/wiki/Insertion_sort).

- [merge_sort.cpp](merge_sort.cpp): Implementation of the Merge Sort algorithm in C++.
  - For more information, see the [Merge Sort Wikipedia article](https://en.wikipedia.org/wiki/Merge_sort).

- [insertion_sort.cpp](insertion_sort.cpp): Implementation of the Insertion Sort algorithm in C++.
  - For more information, see the [Insertion Sort Wikipedia article](https://en.wikipedia.org/wiki/Insertion_sort).

## Contributing

Contributions are welcome! If you have suggestions, improvements, or other sorting algorithms you'd like to add, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
