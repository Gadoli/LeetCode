# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:07:50 2023

@author: david

LeetCode - Easy 1859. Sorting the Sentence

Runtime
36ms
Beats 95.95%of users with Python3

Memory
16.31mb
Beats 36.30%of users with Python3
"""

class Solution:
    def sortSentence(self, s: str) -> str:
        L = s.split(" ")
        R = [""] * len(L)
        for word in L:
            R[int(word[-1]) - 1] = word[:-1]
        return " ".join(R)