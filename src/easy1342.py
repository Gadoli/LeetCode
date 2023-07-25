# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:30:03 2023

@author: david

LeetCode - Easy 1342. Number of Steps to Reduce a Number to Zero


Runtime
35ms
Beats 97.86%of users with Python3

Memory
16.32mb
Beats 24.52%of users with Python3
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        cpt = 0
        while num != 0:
            if num%2==0:
                num = num//2
            else:
                num -= 1

            cpt += 1
        
        return cpt