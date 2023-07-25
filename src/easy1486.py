# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:04:18 2023

@author: david

LeetCode - Easy 1486. XOR Operation in an Array

Runtime
41ms
Beats 84.81%of users with Python3

Memory
16.33mb
Beats 35.86%of users with Python3
"""

from functools import reduce

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2*i)
        
        return reduce(lambda a, b: a ^ b, nums, 0)