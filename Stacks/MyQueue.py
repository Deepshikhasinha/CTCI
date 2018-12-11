# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:03:33 2018

@author: dsinha1
"""

#myQueue: Implement a queue using two stacks



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    
class Stack:
    def __init__(self, root):
        self.root = root
        self.top = root
    
    def push(self, x):
        if(self.top == None):
            self.top = x
            self.root = x
            return
        
        self.top.next = x
        x.next = None
        self.top = x
    
    def pop(self):
        x = self.root
        if x == None:
            return
        if self.root == self.top:
            self.top = None
            self.root= None
            return
        while x.next != self.top:
            x = x.next
        self.top = x
        
    def print_all(self):
        x = self.root
        while(x is not None):
            print(x.val)
            x = x.next

    


class MyQueue:
    def __init__(self, stack1, stack2):
        self.stack1 = stack1
        self.stack2 = stack2
    
    def copy(self, stack1, stack2):
        while stack1.top !=None:
            stack2.push(stack1.top)
            stack1.pop()
            
    def enqueue(self, stack1,val):
        self.stack1.push(val)
        
    def dequeue(self,stack1,stack2):
        self.copy(stack1,stack2)
        #self.stack2.print_all()
        stack2.pop()
        #self.stack2.print_all()
        self.copy(stack2,stack1)
        #self.stack1.print_all()
    
    def print_queue(self):
        self.stack1.print_all()


y = Node(5)
stack1 = Stack(y)
stack2 = Stack(y)
stack2.pop()
queue = MyQueue(stack1,stack2)
queue.enqueue(stack1,Node(7))
queue.enqueue(stack1,Node(3))
queue.enqueue(stack1,Node(2))
queue.enqueue(stack1,Node(1))
queue.enqueue(stack1,Node(4))
queue.enqueue(stack1,Node(8))
queue.print_queue()  
queue.dequeue(stack1,stack2)
queue.dequeue(stack1,stack2)
queue.dequeue(stack1,stack2)
queue.enqueue(stack1,Node(9))
print("--------------------")
queue.print_queue()          
