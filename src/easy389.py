# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:28:22 2022

@author: David

LeetCode - Easy 389. Find the Difference

Idea : get the HashMap of s and t by using Counter
    doing a subtraction of Counter(t) by Counter(s)
    only positive count will remain
    return accordingly a string by using iter() next()

    iter() will be an iterator on keys
    next() works an iterator and return the next value of it, here the first key

Runtime: 45 ms, faster than 76.01% of Python3 online submissions for Find the Difference.
Memory Usage: 13.8 MB, less than 98.45% of Python3 online submissions for Find the Difference.
"""

from collections import Counter

def findTheDifference(s,t):
    return next(iter(Counter(t) - Counter(s)))