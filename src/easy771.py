# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 23:23:27 2022

@author: david

LeetCode - Easy 771. Jewels and Stones

Idea : 
    1 - go through each stone in stones
    2 - check if it's in the jewels set
    3 - if so add to a list 
    4 - return the length of the list

Runtime: 29 ms, faster than 97.21% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.9 MB, less than 59.40% of Python3 online submissions for Jewels and Stones.
"""

def numJewelsInStones(jewels, stones):
    return len([s for s in stones if s in set(jewels)])