# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:33:29 2023

@author: david

LeetCode - Easy 2744. Find Maximum Number of String Pairs


Runtime
Details
52ms
Beats 96.45%of users with Python3

Memory
Details
16.34mb
Beats 44.70%of users with Python3
"""

from collections import Counter
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        C = Counter(sorted([''.join(sorted(word)) for word in words]))
        
        cpt = 0
        for k in C.values():
            if k > 1:
                cpt += 1
                
        return cpt