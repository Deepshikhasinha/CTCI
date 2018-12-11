# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:05:39 2018

@author: dsinha1
"""

#DP - Longest common sequence problem: given 2 strings find the longest common sequence between them.
# A sequence does not need to be consecutive.


def LCS_recursion(str1,str2):
    #print(str1)
    #print(str2)
    if not str1 or not str2:
        return 0
    if str1[len(str1)-1] == str2[len(str2)-1]:
        return 1+ LCS_recursion(str1[:len(str1)-1],str2[:len(str2)-1])
    else:
        return max(LCS_recursion(str1,str2[:len(str2)-1]), LCS_recursion(str1[:len(str1)-1],str2))
    


x = LCS_recursion("ABCDXJ","ACJDTX")
print(x)


# TODO : iterative method
