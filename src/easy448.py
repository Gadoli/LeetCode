# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 22:08:18 2022

@author: david

LeetCode - Easy 448. Find All Numbers Disappeared in an Array
"""

def findDisappearedNumbers(nums):
        """
        # time complexity : O(n)
        # space complexity : O(2n) ?
        
        inspired from my solution on Easy 268. Missing Number
        
        nums will range from 0 to n+1
        so let's create a set that ranges litteraly from 1 to n
            and do the difference with set(nums)
        there should only be numbers that do not appear in nums for the created set
            transform the set to a list and return its unique element
        """
        return list(set([i for i in range(1,len(nums) + 1)]) - set(nums))