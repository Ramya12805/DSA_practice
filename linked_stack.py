#Implementation of linked list using stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListUsingStack:
    def __init__(self):
        self.head = None
        self.stack = []

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        popped_data = self.head.data
        self.head = self.head.next
        self.stack.pop()
        return popped_data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_stack(self):
        print("Stack:", self.stack)


linked_list = LinkedListUsingStack()

linked_list.push(3)
linked_list.push(7)
linked_list.push(10)

linked_list.display()  
linked_list.display_stack() 

popped_element = linked_list.pop()
linked_list.display_stack()  
