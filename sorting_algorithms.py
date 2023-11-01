import numpy as np


class Sorting_Algorithms:

    # Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
    # The array is virtually split into a sorted and an unsorted part.
    # Values from the unsorted part are picked and placed at the correct position in the sorted part.

    # To sort an array of size N in ascending order iterate over the array and compare the current element (key) to its predecessor,
    # if the key element is smaller than its predecessor, compare it to the elements before.
    # Move the greater elements one position up to make space for the swapped element.

    # Time Complexity: O(N^2)
    # Auxiliary Space: O(1)

    @staticmethod
    def insertion_sort(input_list: list) -> list:
        """Sorts a list of elements using the Insertion Sort Algorithm.

        Args:
            input_list (list): Unsorted List of Elements.

        Returns:
            list: Sorted List of Elements.
        """

        for outer_idx in range(1, len(input_list)):
            key = input_list[outer_idx]

            inner_idx = outer_idx - 1

            while inner_idx >= 0 and key < input_list[inner_idx]:
                input_list[inner_idx + 1] = input_list[inner_idx]
                inner_idx -= 1

            input_list[inner_idx + 1] = key

        return input_list

    @staticmethod
    def merge_lists(input_list: list, left_idx: int, right_idx: int, middle_idx: int) -> None:
        """Merges two lists based on their index into one sorted array.

        Args:
            input_list (list): Input List Unsorted
            left_idx (int): Left Index
            right_idx (int): Right Index
            middle_idx (int): Middle Index
        """

        left_list_len = middle_idx - left_idx + 1
        right_list_len = right_idx - middle_idx

        left_array = [input_list[left_idx + i] for i in range(left_list_len)]
        right_array = [input_list[middle_idx + 1 + j]
                       for j in range(right_list_len)]

        i = j = 0
        k = left_idx

        while i < left_list_len and j < right_list_len:
            if left_array[i] <= right_array[j]:
                input_list[k] = left_array[i]
                i += 1

            else:
                input_list[k] = right_array[j]
                j += 1

            k += 1

        while i < left_list_len:
            input_list[k] = left_array[i]
            i, k = i + 1, k + 1

        while j < right_list_len:
            input_list[k] = right_array[j]
            j, k = j + 1, k + 1

    @staticmethod
    def merge_sort(input_list: list, left_idx: int, right_idx: int) -> list:
        """Splits the Array into two and recursively calls Merge sort in both of them and then finally combining both the arrays.

        Args:
            input_list (list): Input List
            left_idx (int): Left Index
            right_idx (int): Right Index
        """

        if left_idx < right_idx:
            middle_idx = left_idx + ((right_idx - left_idx) // 2)

            Sorting_Algorithms.merge_sort(
                input_list=input_list, left_idx=left_idx, right_idx=middle_idx)
            Sorting_Algorithms.merge_sort(
                input_list=input_list, left_idx=middle_idx + 1, right_idx=right_idx)

            Sorting_Algorithms.merge_lists(
                input_list=input_list, left_idx=left_idx, right_idx=right_idx, middle_idx=middle_idx)

    @staticmethod
    def get_partition_index(input_list: list, low_idx: int, high_idx: int) -> int:
        """Gets the partition of the given list taking the last element as the pivot.

        Args:
            input_list (list): Input List
            low_idx (int): Lower Index
            high_idx (int): Higher Index

        Returns:
            int: Partition Index
        """

        pivot_element = input_list[high_idx]

        i = low_idx - 1

        for j in range(low_idx, high_idx):
            if input_list[j] <= pivot_element:
                i = i + 1
                (input_list[i], input_list[j]) = (input_list[j], input_list[i])

        (input_list[i + 1], input_list[high_idx]
         ) = (input_list[high_idx], input_list[i + 1])

        return i + 1

    @staticmethod
    def quick_sort(input_list: list, high_idx: int, low_idx: int) -> None:
        """Uses Quick Sort Approach to sort the list of elements.

        Args:
            input_list (list): Input List
            high_idx (int): Max Index
            low_idx (int): Min Index
        """

        if low_idx < high_idx:
            partition_idx = Sorting_Algorithms.get_partition_index(
                input_list=input_list, low_idx=low_idx, high_idx=high_idx)

            Sorting_Algorithms.quick_sort(
                input_list=input_list, low_idx=low_idx, high_idx=partition_idx - 1)
            Sorting_Algorithms.quick_sort(
                input_list=input_list, low_idx=partition_idx + 1, high_idx=high_idx)


if __name__ == '__main__':
    input_list = list(np.random.randint(low=0, high=1000, size=20))

    print(f'List of Elements before Sorting - {input_list}')

    # Sorting_Algorithms.insertion_sort(input_list=input_list)

    # Sorting_Algorithms.merge_sort(
    #     input_list=input_list, left_idx=0, right_idx=len(input_list) - 1)

    Sorting_Algorithms.quick_sort(
        input_list=input_list, low_idx=0, high_idx=len(input_list) - 1)

    print(f'List of Elements after Sorting - {input_list}')
