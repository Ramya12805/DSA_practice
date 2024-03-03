#implementing BFS(Breadth First Search) in Binary Tree 

from collections import deque

class Node:
    def _init_(self, data):
        self.data = data
        self.prev = None
        self.next = None

class BinaryTree:
    def _init_(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.prev is None:
                        current.prev = new_node
                        break
                    else:
                        current = current.prev
                else:
                    if current.next is None:
                        current.next = new_node
                        break
                    else:
                        current = current.next

    def bfs(self):
        if self.root is None:
            return

        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            print(node.data, end=" ")

            if node.prev:
                queue.append(node.prev)
            if node.next:
                queue.append(node.next)

# Example usage:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(2)
tree.insert(4)
tree.insert(7)
tree.insert(9)

print("BFS:")
tree.bfs()
