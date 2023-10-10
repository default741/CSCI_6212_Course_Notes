import heapq
import timeit
import random
import math

from tqdm import tqdm

import pandas as pd


class Node:

    def __init__(self, freq: int, char: str, left=None, right=None) -> None:
        """Class Initialization Method for Node.

        Args:
            freq (int): Frequency of Character
            char (str): Character to be encoded
            left (_type_, optional): Left pointer to the node. Defaults to None.
            right (_type_, optional): Right Pointer to the node. Defaults to None.
        """

        self.freq = freq
        self.char = char

        self.left = left
        self.right = right

        self.code: str = ''

    def __lt__(self, next) -> bool:
        """Checks if the current node frequency is less than the next node frequency.

        Args:
            next (function): Next Node

        Returns:
            bool: Boolean value of the result.
        """
        return self.freq < next.freq


class HoffmanEncoding:

    @staticmethod
    def encoded_values(current_node: Node, val: str = str()) -> None:
        """Prints Hoffman Encoding Codes for each Character.

        Args:
            current_node (Node): Current Node
            val (str, optional): Hoffman Value. Defaults to ''.
        """

        updated_val = val + str(current_node.code)

        if (current_node.left):
            HoffmanEncoding.encoded_values(current_node.left, updated_val)

        if (current_node.right):
            HoffmanEncoding.encoded_values(current_node.right, updated_val)

        if (not current_node.left and not current_node.right):
            print(f"{current_node.char} => {updated_val}")

    @staticmethod
    def hoffman_encoding(chars: list[str], freq: list[int]) -> None:
        """Encodes a List of characters based on their frequency.

        Args:
            chars (list[str]): List of Characters
            freq (list[int]): Frequency of respective characters
        """

        node_list = []

        for c, f in zip(chars, freq):
            heapq.heappush(node_list, Node(freq=f, char=c))

        while len(node_list) > 1:
            left = heapq.heappop(node_list)
            right = heapq.heappop(node_list)

            left.code = 0
            right.code = 1

            new_node = Node(freq=left.freq + right.freq,
                            char=left.char + right.char, left=left, right=right)

            heapq.heappush(node_list, new_node)

        HoffmanEncoding.encoded_values(node_list[0])


if __name__ == '__main__':
    time_list = []
    n_values = []

    for i in tqdm(range(10)):
        freq_list = []
        char_list = []
        k = math.ceil((i+1)/2)
        l = (i+1) - k

        # for j in range((i + 1) * 3):
        for j in range((5**k)*(2**l)):
            freq_list.append(random.randint(0, 100))
            # char_list.append(chr(65 + j))
            char_list.append(j)

        print(char_list, freq_list)

        start_time = timeit.default_timer()
        HoffmanEncoding.hoffman_encoding(char_list, freq_list)
        end_time = timeit.default_timer()

        time_list.append(end_time - start_time)
        n_values.append(len(char_list))

    pd.DataFrame({'n_values': n_values, 'time_list': time_list}).to_csv(
        './experimental_values_gehna.csv', index=False)
