# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:58:44 2018

@author: dsinha1
"""

#921. Minimum Add to Make Parentheses Valid

stack = []
def valid_paran(S):
    for i in range(len(S)):
        stack.append(S[i])
    j = 0
    while j < len(stack)-1:
        if stack[j] == "(" and stack[j+1] == ")":
            del(stack[j])
            del(stack[j])
            j = 0
        else:
            j += 1
    return len(stack)
print(valid_paran("()))(("))