# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 23:40:22 2022

@author: david

LeetCode - Easy 1662. Check If Two String Arrays are Equivalent
"""

def arrayStringsAreEqual(word1, word2):
    return "".join(word1).__eq__("".join(word2))