# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:11:25 2022

@author: david

LeetCode - Easy 383. Ransom Note

Runtime: 85 ms, faster than 56.78% of Python3 online submissions for Ransom Note.
Memory Usage: 14.2 MB, less than 18.51% of Python3 online submissions for Ransom Note.
"""

from collections import Counter

def canConstruct(ransomNote, magazine):
    return Counter(magazine)>=Counter(ransomNote)