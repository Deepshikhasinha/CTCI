# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:27:17 2018

@author: dsinha1
"""

# Dynamic programming problem : stair case problem.


def find_ways_iterative(n):
    sum_ways = 0
    s = []
    s.append(1)
    s.append(1)
    s.append(2)
    for i in range(3,n+1):
        #print("----"+str(i))
        c = s[i-1] + s[i-2] + s[i-3]
        s.append(c)
    print("Iterative: "+str(s[-1]))


def find_ways_recursion(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    return find_ways_recursion(n-1)+find_ways_recursion(n-2)+find_ways_recursion(n-3)

find_ways_iterative(5)

x = find_ways_recursion(5)
print("Recursion: "+str(x))
    
