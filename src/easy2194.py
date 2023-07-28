# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:26:59 2023

@author: david

LeetCode - Easy 2194. Cells in a Range on an Excel Sheet

Runtime
45ms
Beats 96.15%of users with Python3

Memory
16.39mb
Beats 47.44%of users with Python3
"""

from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        letter_min = ord(s[0])
        letter_max = ord(s[3])
        n_min = int(s[1])
        n_max = int(s[-1])
        R = []
        for c in range(letter_min, letter_max+1):
            for n in range(n_min, n_max+1):
                R.append(chr(c)+str(n))
        return R