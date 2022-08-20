# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:55:16 2022

@author: david

LeetCode - Easy 557. Reverse Words in a String III

Idea : 
    1 - split s by its spaces
    2 - reverse each word from the split
    3 - join the resulting list into a spaced string

Runtime: 66 ms, faster than 49.00% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.6 MB, less than 45.56% of Python3 online submissions for Reverse Words in a String III.
"""

def reverseWords(s):
    return " ".join([word[::-1] for word in s.split(' ')])