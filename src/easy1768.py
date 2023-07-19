# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:54:10 2023

@author: david

LeetCode - Easy 1768. Merge Strings Alternately

Runtime
51ms
Beats 32.87%of users with Python3

Memory
16.42mb
Beats 39.28%of users with Python3
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m =  min(len(word1), len(word2))
        s = ""
        for i in range(m):
            s += word1[i] + word2[i] 
        s += word1[m:] + word2[m:]
        return s