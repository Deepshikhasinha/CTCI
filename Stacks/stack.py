# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:05:55 2018

@author: dsinha1
"""

#Stack implementation

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    
class Stack:
    def __init__(self, root):
        self.root = root
        self.top = root
    
    def push(self, x):
        self.top.next = x
        x.next = None
        self.top = x
    
    def pop(self):
        x = self.root
        while x.next != self.top:
            x = x.next
        self.top = x
    def print_all(self):
        x = self.root
        while(x is not None):
            print(x.val)
            x = x.next

    
y = Node(5)
Stackx = Stack(y)
Stackx.push(Node(7))
Stackx.push(Node(6))
Stackx.push(Node(5))
Stackx.push(Node(4))
Stackx.push(Node(3))
Stackx.print_all()
            
