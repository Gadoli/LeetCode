# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:40:36 2021

LeetCode - Remove One Element to Make the Array Strictly Increasing (easy 1909)

@author: david
"""
import copy

def canBeIncreasing(nums):
    cpt = 0
    for i in range(len(nums)-1):
        if nums[i]>=nums[i+1]:
            #check between 2 by 2 increasing + check not outisde
            cpt+=1
            tmp = i
        if cpt>1:
            return False
    if cpt>1:
        return False
    if cpt==0:
        return True
    if tmp==0:
        return True
    return nums[tmp-1]<=nums[tmp+1]