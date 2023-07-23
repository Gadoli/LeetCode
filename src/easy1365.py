# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 22:38:49 2023

@author: david

LeetCode - Easy 1365. How Many Numbers Are Smaller Than the Current Number


Runtime
59ms
Beats 98.35%of users with Python3

Memory
16.39mb
Beats 70.33%of users with Python3
"""

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        O = sorted(nums)
        S = set(O)
        D = {}

        for n in S:
            D[n] = O.index(n)

        return [D[nums[i]] for i in range(len(nums))]