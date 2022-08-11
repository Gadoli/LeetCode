# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 09:24:34 2022

@author: david

LeetCode - Easy 283. Move Zeroes
"""

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    
    time complexity : O(n)
    space complexity : O(1)
    """
    c = nums.count(0)
    for i in range(c):
        nums.remove(0)
        nums.append(0)
    