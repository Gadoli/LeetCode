# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:14:04 2023

@author: david

LeetCode - Easy 1389. Create Target Array in the Given Order

Runtime
49ms
Beats 58.28%of users with Python3

Memory
16.20mb
Beats 73.75%of users with Python3
"""

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i, n in zip(index, nums):
            target.insert(i, n)

        return target