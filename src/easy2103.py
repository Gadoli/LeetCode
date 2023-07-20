# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:42:22 2023

@author: david

LeetCode - Easy 2103. Rings and Rods


Runtime
47ms
Beats 58.61%of users with Python3

Memory
16.30mb
Beats 70.30%of users with Python3
"""

class Solution:
    def countPoints(self, rings: str) -> int:
        if len(rings)<5:
            return 0

        L = [set() for i in range(10)]
        for i in range(len(rings)):
            if i%2==1:
                L[int(rings[i])].add(rings[i-1])

        cpt = 0
        for s in L:
            if len(s)==3:
                cpt += 1
                
        return cpt

