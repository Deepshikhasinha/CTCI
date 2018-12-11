# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:35:05 2018

@author: dsinha1
"""
arr = [1,2,3,0,2] 
dp_buy = [-1 for i in range(len(arr))]
dp_sell = [-1 for i in range(len(arr))]

def transac(prices,start,buy,cool):
    if buy == True:
        if start >= len(prices)-1:
            return 0
        if dp_buy[start] == -1:
            dp_buy[start] = max(-prices[start] + transac(prices,start+1,False,cool), transac(prices,start+1,True,cool))
        return dp_buy[start]
    else:
        if start >= len(prices) -1:
            return prices[start]
        if dp_sell[start] == -1:
            dp_sell[start] = max(prices[start] + transac(prices,start+cool+1,True,cool), transac(prices,start+1,False,cool))
        return dp_sell[start]
    #return max(b,s)

print(transac(arr,0,True,1))

print(dp_sell)
print(dp_buy)
