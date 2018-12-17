# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:49:18 2018

@author: dsinha1
"""

# Uncommon words from two sentances

#We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

#A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

#Return a list of all uncommon words. 

#You may return the list in any order.


def uncommon_words(A,B):
    a = A.split(" ")
    b = B.split(" ")
    uncommon = {}
    for i in a:
        c = 0
        if i in uncommon:
            c = uncommon[i]
        uncommon[i] = c + 1
    for j in b:
        c = 0
        if j in uncommon:
            c = uncommon[j]
        uncommon[j] = c + 1
    for key in uncommon:
        if uncommon[key] == 1:
            print(key)


uncommon_words("apples are apples not mangoes", "apples are sauce")