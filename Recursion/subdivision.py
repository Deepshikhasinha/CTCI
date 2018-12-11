# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:22:25 2018

@author: dsinha1
"""

def subdivision(array,sub):    
    if not array:
        return len(sub)
        
    if array[0] % max(sub) == 0 or max(sub) % array[0]:
        sub.append(array[0])
        return subdivision(array[1:],sub)
    print(sub)
    return max (subdivision(array[1:],sub), subdivision(array[:len(array)-1],sub))

print( subdivision([10, 5, 3, 15, 20],[1]))
