# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:21:26 2022

@author: david

LeetCode - Easy 1431. Kids With the Greatest Number of Candies
"""

def kidsWithCandies(candies, extraCandies):
    return [candy+extraCandies >= max(candies) for candy in candies]