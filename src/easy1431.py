# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:21:26 2022

@author: david

LeetCode - Easy 1431. Kids With the Greatest Number of Candies
"""

# optimized
def kidsWithCandies(candies, extraCandies):
    m = max(candies)
    return [candy+extraCandies >= m for candy in candies]
