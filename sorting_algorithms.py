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
    def merge_sort(input_list: list) -> list:
        pass


if __name__ == '__main__':
    input_list = np.random.randint(low=0, high=1000, size=20)

    print(f'List of Elements before Sorting - {input_list}')

    sorted_list = Sorting_Algorithms.insertion_sort(input_list=input_list)

    print(f'List of Elements after Sorting - {sorted_list}')
