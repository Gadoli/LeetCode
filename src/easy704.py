# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:26:42 2022

@author: david

LeetCode - Easy 704. Binary Search
"""

def search(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1
        
def search2(nums, target):
    a = 0
    b = len(nums) - 1
    half = b//2
    
    while abs(b-a)>1:
        if nums[half] == target:
            return half
        
        if nums[half] < target:
            a = half
            half = (b - half)//2 + half
            
        else:
            b = half
            half = half - (half - a)//2
            
    if nums[a] == target: return a
    if nums[b] == target: return b
    return -1
             