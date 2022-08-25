# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:05:04 2022

@author: david

LeetCode - Easy 1512. Number of Good Pairs
"""

def numIdenticalPairs(nums):
    c = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]: c+=1
    return c