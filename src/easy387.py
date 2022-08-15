# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 22:16:32 2022

@author: David

LeetCode - Easy 387. First Unique Character in a String

Idea : using Counter, a unique chararcter will have a count of 1
    So we apply Counter to s
    go through each items, and check if a value is equal to 1
    if so return the corresponding index in s
    otherwise return -1

Runtime: 80 ms, faster than 97.24% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.2 MB, less than 18.33% of Python3 online submissions for First Unique Character in a String.
"""

from collections import Counter


def firstUniqChar(s):
    C = Counter(s)
    for k,v in C.items():
        if v==1:
            return s.index(k)
    return -1
        