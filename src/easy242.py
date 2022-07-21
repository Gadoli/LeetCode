# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:05:34 2022

@author: david

LeetCode - Easy 242. Valid Anagram
"""

from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        return Counter(s)==Counter(t)