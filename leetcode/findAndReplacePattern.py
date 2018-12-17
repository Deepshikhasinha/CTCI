# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:32:51 2018

@author: dsinha1
"""

# 890. Find and Replace Pattern

def findAndReplacePattern(words,pattern):
    
    final = []
    for word in words:
        arr1 = [None for i in range(256)]
        arr2 = [None for i in range(256)]
        print(word)
        if len(word) != len(pattern):
            continue
        flag = 0
        for i in range(len(word)):
            
            if arr1[ord(pattern[i])] != None:
                if arr1[ord(pattern[i])] != ord(word[i]):
                    print(pattern[i] +"  " + word[i])
                    flag = 1
                    break
            else:
                arr1[ord(pattern[i])] = ord(word[i])
            if arr2[ord(word[i])] != None:
                if arr2[ord(word[i])] != ord(pattern[i]):
                    print(word[i] +"  " + pattern[i])
                    flag = 1
                    break
            else:
                arr2[ord(word[i])] = ord(pattern[i])
        if flag == 0:
            final.append(word)
    return final

print(findAndReplacePattern( ["ef","fq","ao","at","lx"],"ya"))