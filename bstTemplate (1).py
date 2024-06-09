#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:10:41 2023

@author: vidhyas
"""
import math
class BinarySearchTree:
    """
    This defines the node class. The children can be individually declared or stored
    in a list. We are adding a pos value which stores the nodes position. root nodes pos value is 1
    """
    class node:
        def __init__(self):
            self.element = 0
            self.left = None
            self.right = None
            self.pos = -1
            self.parent = None
    """
        This initializes the binary search tree. ht is the height of the tree, sz is the
        number of nodes. You may define this appropriately.
    """
    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0

    """
        This method implements the functionality of finding an element in the tree. The function
        findElement(e) finds the node in the current tree, whose element is e. Depending on the
        value of e and in relation to the current element visited, the algorithm visits the left
        or the right child till the element is found, or an external node is visited. Your
        algorithm can be iterative or recursive

        Output: Returns the pointer to the node
    """
                 
    def findElement(self,e,curnode):
        if curnode is None or curnode.element==e:
            return curnode
        elif e<curnode.element:
            if curnode.left is None:
                return curnode
            return self.findElement(e,curnode.left)
        else:
            if curnode.right is None:
                return curnode
            return self.findElement(e,curnode.right)
        
            
    """
        This method implements insertion of an element into the binary search tree. Using the
        findElement(e) method find the position to insert, and insert a node with element e,
        as left or right child accordingly. Make sure that you update the value of pos attribute.
        curnode.leftchild.pos = curnode.pos * 2
        curnode.rightchild.pos = curnode.pos * 2 + 1    
    """
    def insertElement(self,e):
        new=self.node()
        new.element=e
        if self.sz==0:
            self.root=new
            new.pos=1
            self.sz+=1
            self.ht=1
        else:
            parent=self.findElement(e,self.root)
            if parent is not None and parent.element==e:
                return
            if e<parent.element:
                parent.left=new
                new.parent=parent
                new.pos=parent.pos*2
            else:
                parent.right=new
                new.parent=parent
                new.pos=parent.pos*2 + 1
            self.sz+=1
            self.ht=max(self.ht,self.findDepth(new.element)+1)
            
    """
        This method inorderTraverse(self,v) performs an inorder traversal of the BST, starting
        from node v which is initially the root and prints the elements of the nodes as they
        are visited. Remember the inorder traversal first visits the left child, followed by
        the parent, followed by the right child. This could be used to print the tree.
    """
    def inorderTraverse(self,v):
    #@start-editable@
        pass
    #@end-editable@

    """
        Given a node v this will return the next element that should be visited after v in the
        inorder traversal. You can define this recursively
    """
    def returnNextInorder(self,node):
        if node.right is not None:
            return self.findElement(self.find_min_element(node.right),node.right)
        p=node.parent
        while p is not None and node==node.right:
            node=p
            p=p.parent
        return p
    """
        This method deleteElement(self, e), removes the node with element e from the tree T.
        There are three cases:
            1. Deleting a leaf or external node:Just remove the node
            2. Deleting a node with one child: Remove the node and replace it with its child
            3. Deleting a node with two children: Instead of deleting the node replace with
                a) its inorder successor node or b)Inorder predecessor node
    """

    def deleteElement(self,e):
        node=self.findElement(e,self.root)
        if node is None:
            return
        if self.isExternal(node):
            if node==node.parent.left:
                node.parent.left=None
            else:
                node.parent.right=None
            self.sz-=1
        elif node.left is None:
            if node==self.root:
                self.root=node.right
            elif node==node.parent.left:
                node.parent.left=node.right
            else:
                node.parent.right=node.right
        elif node.right is None:
            if node==self.root:
                self.root=node.left
            elif node==node.parent.left:
                node.parent.left=node.left
            else:
                node.parent.right=node.left
        else:
            successor=self.returnNextInorder(node)
            node.element=successor.element
            if successor==successor.left:
                successor.parent.left=successor.right
            else:
                successor.parent.right=successor.left
            self.sz-=1
            if successor==successor.parent.left:
                successor.parent.left=None
            else:
                successor.parent.right=None
        self.ht=self.findHeight(self.root)


    """
        There are other support methods which maybe useful for implementing your functionalities.
        These include
            1. isExternal(self,v): which returns true if the node v is external
    """
    def isExternal(self,curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False
    
    def findDepth(self,ele):
        curnode = self.findElement(ele,self.root)
        if(curnode.element != ele):
            print("No such Element")
            return
        else:
            return self.findDepthIter(curnode)
    def findDepthIter(self,curnode):
        depth=0
        while curnode.parent is not None:
            depth+=1
            curnode=curnode.parent
        return depth
    
    def findHeight(self,node):
        if node is None:
            return -1
        else:
            return 1+max(self.findHeight(node.left),self.findHeight(node.right))
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.element,end=" ")
    def preorder(self,root):
        if root is not None:
            print(root.element,end=" ")
            self.preorder(root.left) 
            self.preorder(root.right)
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.element,end=" ")
            self.inorder(root.right)
    def levelorder(self,root):
        if root is not None:
            queue=[root]
            while queue:
                node=queue.pop(0)
                print(node.element,end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    def find_min_element(self,node):
        while node.left is not None:
            node=node.left
        return node.element

def main():
    tree = BinarySearchTree()
    #print("Array Size:")
    arraySize = int(input())
    #print("Array Elements:")
    arr = list(map(int, input().split()))
    for i in range(arraySize):
        tree.insertElement(arr[i])
    """tree.insertElement(50)
    tree.insertElement(20)
    tree.insertElement(70)
    tree.insertElement(1)
    tree.insertElement(10)
    tree.insertElement(90)
    tree.insertElement(15)
    tree.insertElement(30)
    tree.insertElement(60)
    tree.insertElement(61)
    tree.insertElement(62)
    tree.insertElement(65)
    tree.insertElement(8)
    tree.insertElement(100)"""
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="I"):
            tree.inorderTraverse(tree.root)
            print()
        elif(operation[0]=="P"):
            tree.preorderTraverse(tree.root)
            print()
        elif(operation[0]=="Post"):
            tree.postorderTraverse(tree.root)
            print()
        elif(operation[0]=="D"):
            tree.deleteElement(int(operation[1]))
        elif(operation[0]=="H"):
            print(tree.findHeight(int(operation[1])))
        elif(operation[0]=="Depth"):
            print(tree.findDepth(int(operation[1])))
        elif(operation[0]=='Find'):
            key = tree.findElement(int(operation[1]), tree.root)
            if(key.element == int(operation[1])):
                print("Element Found at", key.pos)
            else:
                print("Element not Found")
        elif(operation[0]=="GetC"):
            childs = tree.getChildren(int(operation[1]))
            print(childs)
        inputs-=1

if __name__ == '__main__':
    main()