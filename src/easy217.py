# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:40:35 2022

@author: david

LeetCode - Easy 217. Contains Duplicate
"""

def containsDuplicate(nums):
    my_set = set()
    for i in nums:
        if i in my_set:
            return True
        my_set.add(i)
    return False