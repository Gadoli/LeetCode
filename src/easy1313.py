# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:54:49 2023

@author: david

LeetCode - Easy 1313. Decompress Run-Length Encoded List

"""

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        L = []
        i = 0 
        while i < len(nums):
            L += [nums[i+1]] * nums[i]
            i += 2

        return L