# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:33:25 2018

@author: dsinha1
"""

#Mirror Tree

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:26:39 2018

@author: dsinha1
"""

queue = []
linkedlists = [[]]
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
        print(root.data)
        Tree.traverse(root.left)
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
        #if root.right != None:
       
    def mirror_tree(Tree,root):
        if root == None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        #if mirror_root != None:
        Tree.mirror_tree(root.left)
        Tree.mirror_tree(root.right)
        #mirror_root.left = TreeNode(0)
        #mirror_root.right = TreeNode(0)
        #print(mirror_root.data)
        #if root.right != None and mirror_root != None:
            #Tree.mirror_tree(root.right, mirror_root.left)
        #if root.left != None and mirror_root != None:
            #Tree.mirror_tree(root.left, mirror_root)
        
        
    
        
        
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
#y = x
#Treey = Tree(y)
y = TreeNode(0)
Treex.mirror_tree(x)
#Treex.traverse(x)
#height = Treex.find_height(x)
#print (height)
print("------------------")
Treex.level_traversal(x)
Treez = Tree(z)
#print(y.data)
#print(y.left.data)
#print(y.right.data)
#Treex.traverse(x)




       
