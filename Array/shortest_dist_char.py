# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:20:06 2018

@author: dsinha1
"""
# find the shortest distance between a given character and all characters in the array
indexes = []
distances = []
S = "loveleetcode"
C = "e"
for i in range(len(S)):
    if C == S[i]:
        indexes.append(i)
current = 0
for i in range(len(S)):
    val = []
    for j in indexes:
        if j - i >= 0:
            val.append(j-i)
        else:
            val.append(-1*(j-i))
    distances.append(min(val))
        
print(distances)
        
