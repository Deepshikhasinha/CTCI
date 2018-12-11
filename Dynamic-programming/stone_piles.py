# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:18:04 2018

@author: dsinha1
"""

# stone piles
piles = [1,6,6,9,8,10,5,4]
dp = [[-1 for i in range(len(piles)) ]for j in range(len(piles)) ]
def PredictTheWinner(nums):
       
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1 = sum(nums)
        print(sum1)
        p1 = predict(nums,0,len(nums)-1)
        if(sum1-p1 > p1):
            return False
        else:
            return True
def predict(stones,start,end):
    print(str(start)+"--"+str(end))
    if start > end :
        return 0
    elif start==end:
        dp[start][end] = stones[start]
    elif end == start+1:
        dp[start][end] = max(stones[start],stones[end])
    elif dp[start][end] != -1:
        return dp[start][end]
    else:    
        dp[start][end] = max(min(stones[start]+predict(stones,start+2,end),stones[start]+predict(stones,start+1,end-1)),min(stones[end]+predict(stones,start,end-2),stones[end]+predict(stones,start+1,end-1)))
    return dp[start][end]

print(predict(piles,0,len(piles)-1))
#print(PredictTheWinner(piles))
print(dp[0])
print(dp[1])
print(dp[2])
print(dp[3])
print(dp[4])
print(dp[5])
print(dp[6])
print(dp[7])

#print(PredictTheWinner([1, 5, 233, 7]))
