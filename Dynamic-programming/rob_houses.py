# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 08:54:16 2018

@author: dsinha1
"""

# house robber

#Recursion method
def rob(houses):
    if not houses:
        return 0
    return max((houses[0]+rob(houses[2:])), rob(houses[1:]))



# DP solution:
def rob_dp(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max ( nums[0], nums[1])
        else:
            dp = [0 for i in nums]
        
            dp[1] = max(nums[0], nums[1])
            dp[2] = max ( nums[0]+nums[2], nums[1])
            for i in range(3,len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]  
    
    
print("Recursion:",str(rob([1,2,3,1])))
print("Dp",str(rob_dp([1,2,3,1])))
