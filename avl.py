class AVLTree:
    class Node:
        def __init__(self, element, left=None, right=None):
            self.element=element
            self.left=left
            self.right=right
            self.height=1
            self.sz=0
    def __init__(self):
        #@start-editable@
        self.root=None
        #@end-editable@

    def getHeight(self, node):
        #@start-editable@
        if node is None:
            return
        return node.height
        #@end-editable@

    def getBalance(self, node):
        #@start-editable@
        if node is None:
            return
        return self.getHeight(node.left)-self.getHeight(node.right)
        #@end-editable@

    def rightRotate(self, y):
        #@start-editable@
        x=y.left
        T2=x.right
        x.right=y
        y.left=T2
        y.height=max(self.getHeight(y.left),self.getHeight(y.right))+1
        x.height=max(self.getHeight(x.left),self.getBalance(x.right))+1
        return x
        #@end-editable@

    def leftRotate(self, x):
        #@start-editable@
        y=x.right
        T2=y.left
        y.left=x
        x.right=T2
        x.height=max(self.getHeight(x.left),self.getHeight(x.right))+1
        y.height=max(self.getHeight(y.left),self.getHeight(y.right))+1
        return y
        #@end-editable@

    def insert(self, node, element):
        #@start-editable@
        if node is None:
            return self.Node(element)
        if element<node.element:
            node.left=self.insert(node.left,element)
        elif element>node.element:
            node.right=self.insert(node.right,element)
        else:
            return node

        node.height=1+max(self.getHeight(node.left),self.getHeight(node.right))
        balance=self.getBalance(node)
        if balance>1 and element<node.left.element:
            return self.rightRotate(node)
        if balance<-1 and element>node.right.element:
            return self.leftRotate(node)
        if balance>1 and element>node.left.element:
            node.left=self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance<-1 and element<node.right.element:
            node.right=self.rightRotate(node.right)
            return self.leftRotate(node)
        self.sz+=1
        return node
        #@end-editable@

    def inOrder(self, root):
        #@start-editable@
        if not root:
            return
        self.inOrder(root.left)
        print(root.element,end=" ")
        self.inOrder(root.right)
        #@end-editable@

    def insertElement(self, element):
        #@start-editable@
        return self.insert(self.root,element)
        #@end-editable@

    def get_min_inorder(self,node):
        if node is None or node.left is None:
            return node
        else:
            return self.get_min_inorder(node.left)
    def delete(self,element):
        if self.root:
            self.root=self.deleteElement(element,self.root)
            self.sz-=1
    def deleteElement(self,element,curnode):
        if curnode is None:
            return curnode
        if element<curnode.element:
            curnode.left=self.deleteElement(element,curnode.left)
        elif element>curnode.element:
            curnode.right=self.deleteElement(element,curnode.right)
        else:
            if curnode.left==None:  
                curnode=curnode.right
            elif curnode.right==None:
                curnode=curnode.left
            else:
                successor=self.get_min_inorder(curnode.right)
                curnode.element=successor.element
                curnode.right=self.deleteElement(curnode.element,curnode.right)
        if curnode is None:
            return curnode
        curnode.height=1+max(self.getHeight(curnode.left),self.getHeight(curnode.right))
        balance=self.getBalance(curnode)

        if balance > 1 and self.getBalance(curnode.left) >= 0:
            return self.rightRotate(curnode)
        if balance > 1 and self.getBalance(curnode.left) < 0:
            curnode.left = self.leftRotate(curnode.left)
            return self.rightRotate(curnode)
        if balance < -1 and self.getBalance(curnode.right) <= 0:
            return self.leftRotate(curnode)
        if balance < -1 and self.getBalance(curnode.right) > 0:
            curnode.right = self.rightRotate(curnode.right)
            return self.leftRotate(curnode)
        return curnode
    def printTree(self):
        if not self.root:
            return
        self.levelOrder(self.root)

    def levelOrder(self, root):
        if root is None:
            return
        queue = [root]
        while queue:
            current = queue.pop(0)
            print(current.element, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()
#@start-editable@
# Driver code to demonstrate the usage of AVLTree
if __name__ == "__main__":
    avl = AVLTree()
    elements = [10, 20, 30, 40, 50, 25]
    for element in elements:
        avl.insertElement(element)
    
    print("Inorder traversal of the constructed AVL tree is")
    avl.inOrder(avl.root)
    avl.printTree()
    avl.delete(20)
    avl.printTree()
    avl.printTree()
#@end-editable@
