# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:39:39 2018

@author: dsinha1
"""

#Linked List - reverse

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def insert(self, value):
        node1 = self
        while node1.next is not None:
            node1 = node1.next
        node = Node(value)
        node1.next = node
        node.next = None
            
    def print_list(self):
        node1 = self
        while node1 is not None:
            print(str(node1.data)+" -> "),
            node1 = node1.next
            
class LinkedList:
    def __init__(self,head):
        self.head = head
        
    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            next1 = cur.next
            cur.next =  prev
            prev = cur
            cur = next1
        self.head = prev
    def print_list(self):
        node1 = self.head
        while node1 is not None:
            print(str(node1.data)+" -> "),
            node1 = node1.next
n = Node(1)
n.insert(6)
n.insert(5)
n.insert(3)
n.insert(8)
n.print_list()
print("----------")
l = LinkedList(n)
l.reverse()
l.print_list()
