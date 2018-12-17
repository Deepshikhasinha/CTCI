# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:55:46 2018

@author: dsinha1
"""
n = 17
happy = {}
while (n != 1):
    #print(n)
    if n not in happy:
        happy[n] = 1
    else:
        break
    c = []
    while n > 0:
        c.append(n % 10)
        n = int(n/10)
    x = 0
    for i in c:
        x += i * i
    n = x
    print(x)