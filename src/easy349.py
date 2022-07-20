# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 22:45:54 2022

@author: david

LeetCode - Easy 349. Intersection of Two Arrays
"""

def intersection(nums1, nums2):
    return list(set(nums1).intersection(set(nums2)))
