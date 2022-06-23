# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:24:45 2022

@author: david

LeetCode - Easy 724. Find Pivot Index
"""

def pivotIndex(nums):
    leftSum = 0
    rightSum = sum(nums)
    
    for i in range(len(nums)):
        rightSum -= nums[i]
        
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
        
    return -1