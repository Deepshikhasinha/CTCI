# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:00:42 2018

@author: dsinha1
"""

# tree traversal without recursion

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:26:39 2018

@author: dsinha1
"""

queue = []
linkedlists = [[]]
level = []
rear = 0


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    
class Stack:
    def __init__(self, root):
        self.root = root
        self.top = root
    
    def push(self, x):
        if self.top is None:
            self.top = x
            self.root = x
            x.next = None
            return
        self.top.next = x
        x.next = None
        self.top = x
    
    def pop(self):
        if(self.root == None):
            return
        elif self.root == self.top:
            self.root = None
            self.top = None
        else:
            x = self.root
            while x.next != self.top :
                if x.next !=None:
                    x = x.next
            self.top = x
        
    def print_all(self):
        x = self.root
        while(x is not None):
            print(x.data)
            x = x.next

    def isempty(self):
        if self.top == None:
            return True
        else:
            return False
        
class TreeNode:
    def __init__(self,data = None):
        self.left = None
        self.right = None
        self.data = data
        self.level = 0

class Tree:
    def __init__(self, TreeNode = None):
        self.root = TreeNode
    
    def addNode(Tree, root, TreeNode):
        if TreeNode.data < root.data:
            if root.left != None:
                Tree.addNode(root.left,TreeNode)
            else:
                root.left = TreeNode
                root.left.level = root.level+1
        else:
            if root.right != None:
                Tree.addNode(root.right,TreeNode)
            else:
                root.right = TreeNode
                root.right.level = root.level+1

    def traverse(Tree, root):
        if root == None:
            return
        #if root.left != None:
        level.append(root.level)
        Tree.traverse(root.left)
        Tree.traverse(root.right)
        #print(root.data)
        
        #if root.right != None:
        
        
    def level_traversal(Tree,root):  
        print(str(root.data)+"->"+str(root.level))
        if root.left != None:
            queue.append(root.left)
        if root.right != None:
            queue.append(root.right)
        
        if len(queue) != 0:
            #print(queue[0].data)
            treenode = queue[rear]
            del queue[rear]
            Tree.level_traversal(treenode)
        
    def find_height(Tree,root):
        height = 0
        for i in level:
            if i > height:
                height = i
        return height
    def iterative_traversal(Tree, root):
        current = root
        Stackx = Stack(root)
        Stackx.push(current)
        #current = current.left
        while Stackx.isempty() == False:
            while current is not None:
                current = current.left
                if current is not None:
                    Stackx.push(current)
            current = Stackx.top
            Stackx.pop()
            #Stackx.print_all()
            #print("-----------------")
            print(current.data)
            print("-----------------")
            current = current.right
            if current is not None:
                Stackx.push(current)
        
        
x = TreeNode(5)
Treex = Tree(x)
Treex.addNode(x,TreeNode(7))
Treex.addNode(x,TreeNode(3))
Treex.addNode(x,TreeNode(6))
Treex.addNode(x,TreeNode(1))
Treex.addNode(x,TreeNode(2))
Treex.addNode(x,TreeNode(8))

Treex.iterative_traversal(x)
#height = Treex.find_height(x)
#print (height)
#Treex.level_traversal(x)
