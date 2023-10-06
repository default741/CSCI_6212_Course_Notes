
class SingleNode:

    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = None

    def insert_node_at_begining(self, data: int) -> None:
        new_node = SingleNode(value=data)

        if self.head is None:
            self.head = new_node
            return

        else:
            new_node.next = self.head
            self.head = new_node

    def insert_node_at_index(self, data: int, idx: int) -> None:
        new_node = SingleNode(value=data)
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
                current_node.next = new_node

            else:
                print(f'Index ({idx}) not present!')

    def insert_node_at_end(self, data: int) -> None:
        new_node = SingleNode(value=data)

        if self.head is None:
            self.head = new_node
            return

        currrent_node = self.head

        while currrent_node.next is not None:
            currrent_node = currrent_node.next

        currrent_node.next = new_node

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

    def remove_last_node(self) -> None:
        if self.head is not None:

            current_node = self.head

            while current_node.next.next is not None:
                current_node = current_node.next

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
                    current_node.next = current_node.next.next

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
                current_node.next = current_node.next.next

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
    singly_linked_list = SinglyLinkedList()

    singly_linked_list.insert_node_at_end(data=1)
    singly_linked_list.insert_node_at_begining(data=2)
    singly_linked_list.insert_node_at_index(data=3, idx=1)

    singly_linked_list.insert_node_at_index(data=3, idx=1)
    singly_linked_list.insert_node_at_index(data=4, idx=2)
    singly_linked_list.insert_node_at_index(data=5, idx=0)
    singly_linked_list.insert_node_at_index(data=6, idx=2)
    singly_linked_list.insert_node_at_index(data=7, idx=3)

    singly_linked_list.print_linked_list()
    print(singly_linked_list.get_size())

    singly_linked_list.update_node_at_index(data=9, idx=7)

    singly_linked_list.print_linked_list()
    print(singly_linked_list.get_size())

    singly_linked_list.remove_first_node()
    singly_linked_list.remove_last_node()
    singly_linked_list.remove_node_at_idx(idx=3)
    singly_linked_list.remove_node_with_value(value=10)

    singly_linked_list.print_linked_list()
    print(singly_linked_list.get_size())

