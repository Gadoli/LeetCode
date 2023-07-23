# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 22:55:07 2023

@author: david

LeetCode - Easy 2413. Smallest Even Multiple

"""

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1)