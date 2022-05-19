# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:33:47 2021

LeetCode - Max Consecutive Ones (easy 485)

@author: david
"""


def findMaxConsecutiveOnes(nums):
    cpt = 0
    R = 0
    length = len(nums)
    
    for i in range(length):
        if nums[i]==1:
            cpt+=1
        else:
            if cpt > R:
                R = cpt
            if (length-i)<R:
                break
            cpt=0
            
    if cpt > R:
        R = cpt
    return R

print(findMaxConsecutiveOnes([0,1,1,1,1,0]))