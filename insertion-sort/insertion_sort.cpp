#include <cstdio>

void insertion_sort(int* array, int size) {
    int i, j, value;
    for (i = 0; i < size; i++) {
        value = array[i];
        j = i - 1;
        while (j >= 0 && array[j] > value) {
            array[j + 1] = array[j];
            j--;
        }
        array[j + 1] = value;
    }
}

int main() {
    int i, length;
    std::printf("Length of array to sort: ");
    std::scanf("%d", &length);
    int array1[length];
    std::printf("Enter each element in the array separated by spaces, then click enter:\n");
    
    std::getchar();

    for (i = 0; i < length; i++) {
        std::scanf("%d", &array1[i]);
    }

    std::getchar();

    insertion_sort(array1, sizeof(array1) / sizeof(array1[0]));

    std::printf("{");
    for (int i = 0; i < sizeof(array1) / sizeof(array1[0]); i++) {
        std::printf("%d", array1[i]);

        if (i != sizeof(array1) / sizeof(array1[0]) - 1) {
            std::printf(", ");
        }
    }
    std::printf("}");
}
