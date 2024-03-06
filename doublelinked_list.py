class Node:
    def __init__(self, data):
        self.element = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def list_size(self):
        return self.size

    def insert_first(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_last(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
        self.size += 1

    def delete_first(self):
        if self.size == 0:
            print("List is empty")
        else:
            temp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            del temp
            self.size -= 1

    def delete_last(self):
        if self.size == 0:
            print("List is empty")
        elif self.size == 1:
            self.delete_first()
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.prev.next = None
            del current_node
            self.size -= 1

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.element, end=" ")
            current_node = current_node.next
        print("")

    def print_list_reverse(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        while current_node:
            print(current_node.element, end=" ")
            current_node = current_node.prev
        print("")


dll = DoublyLinkedList()
