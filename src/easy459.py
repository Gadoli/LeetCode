# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:16:14 2024

@author: david

LeetCode - Easy 459. Repeated Substring Pattern

"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        if s in t [1:-1]:
            return True
        return False


"""
First solution

from itertools import groupby

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        def chunks(lst, n):
            return [lst[i:i + n] for i in range(0, len(lst), n)]

        def all_equal(iterable):
            g = groupby(iterable)
            return next(g, True) and not next(g, False)

        for a in range(1, len(s)//2 + 1):
            if all_equal(chunks(s, a)):
                return True

        return False
"""