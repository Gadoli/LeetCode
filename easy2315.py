# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 22:23:13 2023

@author: david

LeetCode - Easy 2315. Count Asterisks
"""

class Solution:
    def countAsterisks(self, s: str) -> int:
        r = 0
        M = s.split("|")
        for i in range(len(M)):
            if i%2==0:
                r += M[i].count("*")
        return r