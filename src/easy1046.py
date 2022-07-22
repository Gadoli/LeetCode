# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:35:17 2022

@author: david

LeetCode - Easy 1046. Last Stone Weight

Runtime: 63 ms, faster than 15.74% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.9 MB, less than 61.83% of Python3 online submissions for Last Stone Weight.
"""

def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort()
        tmp = abs(stones[-1] - stones[-2])
        stones.pop()
        stones.pop()
        if tmp: stones.append(tmp)
    if stones:
        return stones[0]
    return 0