# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 22:18:48 2023

@author: david

LeetCode - Easy 2574. Left and Right Sum Differences
"""

from typing import List
import numpy as np

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # L = np.cumsum(nums)
        # R = np.cumsum(nums[::-1])[::-1]

        return list(np.absolute(np.cumsum(nums) - np.cumsum(nums[::-1])[::-1]))