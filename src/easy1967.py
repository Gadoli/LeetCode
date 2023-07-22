# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 16:31:04 2023

@author: david

LeetCode - Easy 1967. Number of Strings That Appear as Substrings in Word
"""
from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cpt = 0
        for pat in patterns:
            if pat in word:
                cpt += 1
        return cpt