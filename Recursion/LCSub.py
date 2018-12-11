# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:16:07 2018

@author: dsinha1
"""

# DP - Longest common substring 

def LCSub(str1,str2,sub):
    if not str1 or not str2:
        return sub
    
    if len(str1) == 1 or len(str2) == 1:
        if str1[0] == str2[0]:
            return sub +1
        else:
            return sub
        
    if str1[0] == str2[0]:
        sub = sub+1
        return LCSub(str1[1:],str2[1:],sub)
    else:
        return max ( LCSub(str1,str2[1:],sub), LCSub(str1[1:],str2,sub))
        

x = LCSub("abcdxyz", "xyzabcd", 0)
print(x)
