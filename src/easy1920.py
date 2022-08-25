# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:16:30 2022

@author: david

LeetCode - Easy 1920. Build Array from Permutation
"""

def buildArray(nums):
    return (nums[nums[i]] for i in range(len(nums)))