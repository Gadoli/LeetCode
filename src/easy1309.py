# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 16:42:08 2023

@author: david

LeetCode - Easy 1309. Decrypt String from Alphabet to Integer Mapping
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        def transform(n: int) -> str:
            return chr(ord('a') + n - 1)

        res = ""
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2]=='#':
                res += transform( int(s[i] + s[i+1]) )
                i += 3

            else:
                res += transform(int(s[i]))
                i += 1
        
        return res