class Node:

    def __init__(self, value: int) -> None:
        self.previous = None
        self.value = value
        self.next = None


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None

    def insert_node_at_begining(self, data: int) -> None:
        new_node = Node(value=data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert_node_at_index(self, data: int, idx: int) -> None:
        new_node = Node(value=data)
        current_node = self.head
        position = 0

        if position == idx:
            self.insert_node_at_begining(data=data)

        else:
            while current_node is not None and position + 1 != idx:
                position += 1
                current_node = current_node.next

            if current_node is not None:
                new_node.next = current_node.next
                current_node.next.previous = new_node
                new_node.previous = current_node
                current_node.next = new_node

            else:
                print(f'Index ({idx}) not present!')

    def insert_at_end(self, data: int) -> None:
        new_node = Node(value=data)

        if self.head is None:
            self.head = new_node

        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.previous = current_node

    def update_node_at_index(self, data: int, idx: int) -> None:
        current_node = self.head
        position = 0

        if position == idx and current_node is not None:
            current_node.value = data

        else:
            while current_node is not None and position != idx:
                position += 1
                current_node = current_node.next

            if current_node is not None:
                current_node.value = data

            else:
                print(f'Index ({idx}) not present!')

    def remove_first_node(self) -> None:
        if self.head is not None:
            self.head = self.head.next
            self.head.previous = None

    def remove_last_node(self) -> None:
        if self.head is not None:
            current_node = self.head

            while current_node.next.next is not None:
                current_node = current_node.next

            current_node.next.previous = None
            current_node.next = None

    def remove_node_at_idx(self, idx: int) -> None:
        if self.head is not None:
            current_node = self.head
            position = 0

            if position == idx:
                self.remove_first_node()

            else:
                while current_node.next is not None and position + 1 != idx:
                    position += 1
                    current_node = current_node.next

                if current_node is not None:
                    current_node.next.previous = None
                    current_node.next = current_node.next.next
                    current_node.next.previous.next = None
                    current_node.next.previous = current_node

                else:
                    print(f'Index ({idx}) not present!')

    def remove_node_with_value(self, value: int) -> None:
        if self.head is not None:
            current_node = self.head

            if current_node.value == value:
                self.head = current_node.next
                return

            while current_node.next is not None and current_node.next.value != value:
                current_node = current_node.next

            if current_node is not None:
                current_node.next.previous = None
                current_node.next = current_node.next.next
                current_node.next.previous.next = None
                current_node.next.previous = current_node

            else:
                print(f'Data ({value}) not present!')


    def get_size(self) -> int:
        size = 0

        if self.head is not None:
            current_node = self.head

            while current_node is not None:
                size += 1
                current_node = current_node.next

            return size

        else:
            return 0

    def print_linked_list(self) -> None:
        current_node = self.head

        while current_node is not None:
            print(current_node.value, end=' ')

            current_node = current_node.next

        print()



if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.insert_node_at_begining(data=1)
    doubly_linked_list.insert_node_at_begining(data=2)

    doubly_linked_list.insert_node_at_index(data=3, idx=1)
    doubly_linked_list.insert_node_at_index(data=4, idx=2)

    doubly_linked_list.insert_at_end(data=5)
    doubly_linked_list.insert_at_end(data=6)

    doubly_linked_list.print_linked_list()
    print(doubly_linked_list.get_size())

    doubly_linked_list.update_node_at_index(data=44, idx=2)

    doubly_linked_list.print_linked_list()
    print(doubly_linked_list.get_size())
