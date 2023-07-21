# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:59:10 2023

@author: david

LeetCode - Easy 2418. Sort the People

Runtime
132ms
Beats 64.40%of users with Python3

Memory
16.90mb
Beats 37.34%of users with Python3
"""

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Normal writting
        """
        D = dict()
        for i in range(len(heights)):
            D[heights[i]] = i        

        L = [v for k, v in sorted(D.items(), key=lambda item: item[0], reverse=True)]

        return [names[i] for i in L]
        """
        
        # condensed
        return [names[i] for i in [v for k, v in sorted({heights[i]: i for i in range(len(heights))}.items(), key=lambda item: item[0], reverse=True)]]