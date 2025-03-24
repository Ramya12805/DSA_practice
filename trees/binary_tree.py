import math
from collections import deque

class BinaryTree:

    class Node:
        def __init__(self):
            self.element = None
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None
        self.sz = None

    def inorderTraverse(self, root):
        if not root:
            return None
        self.inorderTraverse(root.left)
        print(root.val, end=" ")
        self.inorderTraverse(root.right)

    def preorderTraverse(self, root):    
        if not root:
            return None
        print(root.val, end=" ")
        self.preorderTraverse(root.left)
        self.preorderTraverse(root.right)

    def postorderTraverse(self, root):
        if not root:
            return None
        self.postorderTraverse(root.left)
        self.postorderTraverse(root.right)
        print(root.val, end=" ")

    def findDepth(self, x):
        return self.depth(self.root, x)

    def depth(self, root, x):
        if not root:
            return -1
        queue = [root]
        totaldepth = 0
        while queue:
            node = queue.pop(0)
            if node.val == x.val:
                return totaldepth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            totaldepth += 1
        return -1

    def height(self, root, x):
        if not root:
            return -1
        queue = [root]
        totalheight = 0
        while queue:
            node = queue.pop(0)
            if node.val == x.val:
                return self.height_of_tree(self.root) - totalheight
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            totalheight += 1
        return -1

    def findHeight(self, x):
        return self.height(self.root, x)

    def height_of_tree(self, root):
        if not root:
            return None
        return 1 + max(self.height_of_tree(root.left), self.height_of_tree(root.right))

    def levelorderTraverse(self, root):
        if not root:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def printCurrentLevel(self, root, level):
        if not root:
            return None
        l = 0
        queue = [root]
        while queue:
            y = []
            node = queue.pop(0)
            y.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if l == level:
                break
            else:
                l += 1
        print(y)

    def isPerfect(self, root):
        if not root:
            return None
        l = 0
        queue = [root]
        while queue:
            nodes_count = len(queue)
            if nodes_count != 2**l:
                return False
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            l += 1
        return True

    def buildTree(self, eltlist):
        if not eltlist:
            return None
        nodes = [None]*len(eltlist)
        for i in range(len(eltlist)):
            nodes[i] = self.Node()
            nodes[i].val = eltlist[i]

        for i in range(len(eltlist)):
            if len(eltlist) > 2*i+1 and eltlist[2*i+1] != -1:
                nodes[i].left = nodes[2*i+1]
            if len(eltlist) > 2*i+2 and eltlist[2*i+1] != -1:
                nodes[i].right = nodes[2*i+2]
        self.root = nodes[0]
        return nodes

    def insertAfterPosition(self, pos, val):
        new_node = self.Node()
        new_node.val = val
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.val == pos:
                if not node.right:
                    node.right = new_node
                    new_node.parent = node
                    return
                else:
                    new_node.right = node.right
                    node.right.parent = new_node
                    node.right = new_node
                    new_node.parent = node
                    return
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def deleteAfterPosition(self, pos):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.val == pos:
                if node.right:
                    temp = node.right
                    if temp.left is None:
                        node.right = temp.right
                        if temp.right:
                            temp.right.parent = node
                    else:
                        while temp.left is not None:
                            temp = temp.left
                        temp.parent.left = temp.right
                        if temp.right:
                            temp.right.parent = temp.parent
                    return
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def printSiblings(self, val):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                if node.parent:
                    if node.parent.left == node:
                        if node.parent.right:
                            print(node.parent.right.val)
                        else:
                            print("No sibling found")
                    elif node.parent.right == node:
                        if node.parent.left:
                            print(node.parent.left.val)
                        else:
                            print("No sibling found")
                else:
                    print("No parent found for the given node")
                return
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print("Node not found in the tree")

    def printAncestors(self, val):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                ancestors = []
                while node.parent:
                    ancestors.append(node.parent.val)
                    node = node.parent
                if ancestors:
                    print(" ".join(map(str, ancestors)))
                else:
                    print("No ancestors found")
                return
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print("Node not found in the tree")

    def printDescendants(self, val):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                descendants = []
                self.getDescendants(node, descendants)
                if descendants:
                    print(" ".join(map(str, descendants)))
                else:
                    print("No descendants found")
                return
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print("Node not found in the tree")

    def getDescendants(self, node, descendants):
        if node:
            if node.left:
                descendants.append(node.left.val)
                self.getDescendants(node.left, descendants)
            if node.right:
                descendants.append(node.right.val)
                self.getDescendants(node.right, descendants)


# Driver code - DO NOT EDIT
def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if operation[0] == "IN":
            tree.inorderTraverse(tree.root)
            print()
        elif operation[0] == "PR":
            tree.preorderTraverse(tree.root)
            print()
        elif operation[0] == "PO":
            tree.postorderTraverse(tree.root)
            print()
        elif operation[0] == "L":
            tree.levelorderTraverse(tree.root)
            print()
        elif operation[0] == "D":
            pos = int(operation[1])
            print(tree.findDepth(nlist[pos]))
        elif operation[0] == "H":
            pos = int(operation[1])
            print(tree.findHeight(nlist[pos]))
        elif operation[0] == "PERFECT":
            print(tree.is_perfect(tree.root))
        elif operation[0] == "IA":
            pos, val = map(int, operation[1:])
            tree.insertAfterPosition(pos, val)
        elif operation[0] == "DA":
            pos = int(operation[1])
            tree.deleteAfterPosition(pos)
        elif operation[0] == "SI":
            val = int(operation[1])
            tree.printSiblings(val)
        elif operation[0] == "AN":
            val = int(operation[1])
            tree.printAncestors(val)
        elif operation[0] == "DE":
            val = int(operation[1])
            tree.printDescendants(val)
        inputs -= 1

if __name__ == '__main__':
    main()