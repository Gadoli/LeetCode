# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:14:26 2023

@author: david

LeetCode - Easy 2367. Number of Arithmetic Triplets

"""

from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cpt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        cpt+=1
        return cpt