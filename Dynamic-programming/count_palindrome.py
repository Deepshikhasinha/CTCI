# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:29:27 2018

@author: dsinha1
"""

def count(string):
    if not string:
        return 0
    if ispalindrom(string):
        return 1 + count(string[:len(string)-1])   + count(string[1:]) - count(string[1:len(string)-1])
    else :
        return count(string[:len(string)-1])  + count(string[1:])  - count(string[1:len(string)-1])

def ispalindrom(st):
    i = 0
    j = len(st)-1
    while( i <= j):
        if st[i] != st[j]:
            return False
        i += 1
        j -= 1
    
    return True


#dp method
def dp_count(string):
    if not string:
        return 0
    dict dictionary = {}
    dictionary[string[0]] = 1
    dictionary
print(ispalindrom("a"))
print(count("abba"))
    
