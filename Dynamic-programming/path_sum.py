# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:48:42 2018

@author: dsinha1
"""

#min sum path
arr = [[1,2],[5,3],[2,1]]#[[1,3,1],[1,5,1],[4,2,1]]
dp = [[-1 for i in range(len(arr[0])) ]for j in range(len(arr)) ]

def min_path(arr,x,y,rec):
    #if x == 0 and y == 0:
     #   dp[x][y] = arr[x][y]
    
    
    if x == 0 and y ==0: #len(arr)-1 and y == len(arr[0])-1:
        dp[x][y] = arr[x][y]
    elif x < 0 and y < 0:
        return 0
    elif(dp[x][y] != -1):
        return dp[x][y]
    elif y == 0: #len(arr[0])-1 :
        dp[x][y] = arr[x][y] + min_path(arr,x-1,y,rec+1)
    elif x == 0: #len(arr)-1:
        dp[x][y] = arr[x][y] + min_path(arr,x,y-1,rec+1)
    #print(arr[x][y])
    else :
        dp[x][y] = arr[x][y]+min(min_path(arr,x-1,y,rec+1),min_path(arr,x,y-1,rec+1))
    print(str(x)+"---"+str(y))
    return dp[x][y]
    #print (x)
    #return x
print(dp)  
print(len(arr)-1)
print(len(arr[0])-1)
print(min_path(arr,len(arr)-1,len(arr[0])-1,0))
print(dp)
