from typing import Union


class Point:

    def __init__(
        self,
        x_coordinate: Union[int, float],
        y_coordinate: Union[int, float]
    ) -> None:

        self.x = x_coordinate
        self.y = y_coordinate


class Node:

    def __init__(self, data: Union[int, float, str]) -> None:
        self.data = data
        self.next_node = None
        self.prev_node = None


set_data_structure = {1, 2, 3, 4, 5, 6, 7}
print(set_data_structure)  # Output: {1, 2, 3, 4, 5, 6, 7}

set_data_structure.add(8)
print(set_data_structure)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

print(set_data_structure.__contains__(6))  # Output: True
print(set_data_structure.__contains__(9))  # Output: False
