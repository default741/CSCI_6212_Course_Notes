import numpy as np


class Searching_Algorithms:

    # Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.
    # The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N).
    # To apply Binary Search algorithm:
    #   The data structure must be sorted.
    #   Access to any element of the data structure takes constant time.

    @staticmethod
    def binary_search_iterative(input_list: list, left_idx: int, right_idx: int, value: int) -> int:
        """Searches an element in a list using Binary Search Algorithm Iteratively.

        Args:
            input_list (list): Sorted Input List.
            left_idx (int): Leftmost Index of the input_list.
            right_idx (int): Rightmost Index of the input_list.
            value (int): Element to be searched in the list.

        Returns:
            int: Index Value.
        """

        while left_idx <= right_idx:
            midpoint_idx = left_idx + ((right_idx - left_idx) // 2)

            if input_list[midpoint_idx] == value:
                return midpoint_idx

            elif input_list[midpoint_idx] < value:
                left_idx = midpoint_idx + 1

            else:
                right_idx = midpoint_idx - 1

        return -1

    @staticmethod
    def binary_search_recursive(input_list: list, left_idx: int, right_idx: int, value: int) -> list:
        """Searches an element in a list using Binary Search Algorithm Recursively.

        Args:
            input_list (list): Sorted Input List.
            left_idx (int): Leftmost Index of the input_list.
            right_idx (int): Rightmost Index of the input_list.
            value (int): Element to be searched in the list.

        Returns:
            int: Index Value.
        """

        if left_idx > right_idx:
            return -1

        midpoint_idx = left_idx + ((right_idx - left_idx) // 2)

        if input_list[midpoint_idx] == value:
            return midpoint_idx

        elif input_list[midpoint_idx] < value:
            return Searching_Algorithms.binary_search_recursive(input_list=input_list, left_idx=midpoint_idx + 1, right_idx=right_idx, value=value)

        else:
            return Searching_Algorithms.binary_search_recursive(input_list=input_list, left_idx=left_idx, right_idx=midpoint_idx - 1, value=value)


if __name__ == '__main__':
    input_list = sorted(np.random.randint(low=0, high=100, size=50))
    value = np.random.randint(low=0, high=100)

    print(f'Input List - {input_list}')
    print(f'Value to Search - {value}')

    value_idx_itr = Searching_Algorithms.binary_search_iterative(
        input_list=input_list, left_idx=0, right_idx=len(input_list) - 1, value=value)
    value_idx_rec = Searching_Algorithms.binary_search_recursive(
        input_list=input_list, left_idx=0, right_idx=len(input_list) - 1, value=value)

    if value_idx_itr == -1:
        print(f'Value ({value}) Not Found in the Input List.')

    else:
        print(f'Value ({value}) Found at Index: {value_idx_itr}')

    if value_idx_rec == -1:
        print(f'Value ({value}) Not Found in the Input List.')

    else:
        print(f'Value ({value}) Found at Index: {value_idx_rec}')
