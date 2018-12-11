# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:34:56 2018

@author: dsinha1
"""arr = [1,2,3,0,2 ] 
dp_buy = [-1 for i in range(len(arr))]
dp_sell = [-1 for i in range(len(arr))]

def transac(prices,start,buy,fee):
    if buy == True:
        if start == len(prices)-1:
            return 0
        if dp_buy[start] == -1:
            dp_buy[start] = max(-prices[start] + transac(prices,start+1,False,fee), transac(prices,start+1,True,fee))
        return dp_buy[start]
    else:
        if start == len(prices) -1:
            return prices[start] - fee
        if dp_sell[start] == -1:
            dp_sell[start] = max(prices[start] - fee + transac(prices,start+1,True,fee), transac(prices,start+1,False,fee))
        return dp_sell[start]
    #return max(b,s)

print(transac(arr,0,True,6806))

print(dp_sell)
print(dp_buy)
