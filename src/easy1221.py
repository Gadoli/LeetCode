# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:59:29 2023

@author: david

LeetCode - Easy 1221. Split a String in Balanced Strings

"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        tmp = 0
        cpt = 0
        for i in s:
            if i=="R":
                tmp += 1
            else:
                tmp -= 1
            
            if tmp == 0:
                cpt += 1
        
        return cpt