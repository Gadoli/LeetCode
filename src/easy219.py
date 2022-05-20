# -*- coding: utf-8 -*-
"""
Created on Fri May 20 14:57:25 2022

@author: david

LeetCode - Easy 219. Contains Duplicate II
"""

# Not the most efficient way

def containsNearbyDuplicate(nums, k):
    my_dict = dict()
    for i in range(len(nums)):
        if nums[i] in my_dict:
            print(my_dict)
            for j in my_dict[nums[i]]:
                if abs(i - j) <= k:
                    return True
            my_dict[nums[i]].append(i)
        else:    
            my_dict[nums[i]] = [i]
    return False