# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:15:48 2023

@author: david

LeetCode - Easy 1688. Count of Matches in Tournament

Runtime
26 ms
Beats
93.47%

Memory
13.8 MB
Beats
94.20%
"""

class Solution:
    def numberOfMatches(self, n: int) -> int:
        tmp = n
        r = 0
        while (tmp>1):
            if tmp%2==0:
                r += tmp//2
                tmp = tmp//2
            else:
                r += (tmp-1)//2
                tmp = (tmp-1)//2 +1
        return r

