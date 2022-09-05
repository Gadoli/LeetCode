# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:12:23 2022

@author: david

LeetCode - Easy 1827. Minimum Operations to Make the Array Increasing

(not a good indicator though since online submissions differs from one to another...)
Runtime: 126 ms, faster than 98.53% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
Memory Usage: 14.6 MB, less than 90.35% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
"""


def minOperations(nums):
    cpt = 0
    for i in range(1,len(nums)):
        if nums[i]>nums[i-1]: continue
        tmp = nums[i-1] - nums[i] + 1    
        cpt += tmp
        nums[i] += tmp
    return cpt
        
         

