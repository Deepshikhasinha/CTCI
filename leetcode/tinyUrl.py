# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:05:04 2018

@author: dsinha1
"""
longUrl = "https://leetcode.com/problems/design-tinyurl"
x = longUrl.encode(encoding='ascii',errors='strict')
print (x)
y = x.decode('ascii')
print(y)