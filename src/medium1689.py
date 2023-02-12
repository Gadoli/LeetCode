# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:58:32 2023

@author: david

LeetCode - Medium 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

Runtime
35 ms
Beats
98.90%
Memory
14.7 MB
Beats
48.6%
"""

def minPartitions(n: str) -> int:
    for i in range(9, 0, -1):
        if str(i) in n: return i
    return 0