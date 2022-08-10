# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 23:07:31 2022

@author: david

LeetCode - Easy 268. Missing Number
"""


# first solution
def missingNumber(nums):
    # time complexity : O(n)
    # space complexity : O(2n) ?
    
    """
    nums will range from 0 to n+1 but one number will be missing
    so let's create a set that ranges litteraly from 0 to n+1
        and do the difference with set(nums)
    there should be only one number left for the created set
        transform the set to a list and return its unique element
    """
    length = len(nums) + 1
    return list(set([i for i in range(length)]) - set(nums))[0]
    