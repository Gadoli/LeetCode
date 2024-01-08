# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:53:01 2024

@author: david

LeetCode - Easy 1822. Sign of the Product of an Array
"""

from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        r = 1
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                r = r * (-1)
        return r