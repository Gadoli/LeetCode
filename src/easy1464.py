# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 20:04:28 2023

@author: david

LeetCode - Easy 1464. Maximum Product of Two Elements in an Array

Runtime
66ms
Beats 62.14%of users with Python3

Memory
16.47mb
Beats 28.62%of users with Python3
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        L = sorted(nums, reverse=True)
        return (L[0] - 1) * (L[1] - 1)