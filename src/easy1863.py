# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 20:44:01 2023

@author: david

LeetCode - Easy 1863. Sum of All Subset XOR Totals
"""

from typing import List

from functools import reduce
import operator
from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # getting all nums combinations
        list_combinations = list()
        for n in range(len(nums) + 1):
            list_combinations += list(combinations(nums, n))

        L = [sub for sub in list_combinations if len(sub)>1]
        
        # single subsets
        r = sum(nums)

        # XOR to all subsets of length > 1 in nums
        for sub in L:
            r += reduce(operator.xor, sub)
        
        return r