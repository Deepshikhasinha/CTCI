# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:28:48 2018

@author: dsinha1
"""

# choice area


def area(A,B,change,c):
    print(c)
    if A < 0 or B < 0:
        return c-1
    
    if change == 0:
        return max (area(A+3,B+2,1,c+1), area(A-5,B-10,2,c+1), area(A-20,B+5,3,c+1))
    elif change == 1:
        return max ( area(A-5,B-10,2,c+1), area(A-20,B+5,3,c+1))
    elif change == 2:
        return max ( area(A+3,B+2,1,c+1), area(A-20,B+5,3,c+1))
    elif change == 3:
        return max ( area(A+3,B+2,1,c+1), area(A-5,B-10,2,c+1))
    
print(area(20,8,0,0))
    
    
