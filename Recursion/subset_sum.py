# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:08:45 2018

@author: dsinha1
"""

# subset sum problem
# given a set find if any of its subset sum equals a given value

def subset_sum(array,summation):
    s = 0
    print(summation)
    if summation == 0:
        return True
    if summation < 0 :
        return False
    print(array)
    if not array:
        return False
    size = len(array)
    return subset_sum(array[:size-1],summation) or subset_sum(array[:size-1],summation-array[len(array)-1])

a = [1, 13, 12, 5, 2]
x = 9
print(subset_sum(a,x))
