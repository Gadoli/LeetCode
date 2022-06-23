# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:33:47 2022

@author: david

LeetCode - Easy 1480. Running Sum of 1d Array
"""

def runningSum(nums):
    sum = 0
    R = []
    for i in nums:
        sum += i
        R.append(sum)
    return R