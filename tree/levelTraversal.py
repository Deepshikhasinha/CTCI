# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:26:39 2018

@author: dsinha1
"""

queue = []
rear = 0
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
        Tree.traverse(root.left)
        print(root.data)
        #if root.right != None:
        Tree.traverse(root.right)
        
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
        
        
        
x = TreeNode(5)
Treex = Tree(x)
Treex.addNode(x,TreeNode(7))
Treex.addNode(x,TreeNode(3))
Treex.addNode(x,TreeNode(6))
Treex.addNode(x,TreeNode(1))
Treex.addNode(x,TreeNode(2))
Treex.addNode(x,TreeNode(8))
#Treex.traverse(x)
Treex.level_traversal(x)
