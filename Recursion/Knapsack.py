# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:30:30 2018

@author: dsinha1
"""

# DP - Knapsack problem

v = [60,100,120]
w = [10,20,30]
weight = 50

def knap(v,w,weight,value,rlevel):
    print("value:"+str(value))
    print("recursion:"+str(rlevel))
    
    if not v:
        return value
    if len(w) == 1 and w[0] > weight:
        return value
    if len(w) == 1 and w[0] <= weight:
        return value + v[0]
    
    if weight - w[0] <= 0:
        return knap(v[1:],w[1:],weight,value,rlevel+1)
    
    return max (knap(v[1:],w[1:],weight-w[0],value+v[0],rlevel+1),knap(v[1:],w[1:],weight,value,rlevel+1))


z = knap (v,w,weight,0,0)
print(z)
