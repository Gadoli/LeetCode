# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 21:00:07 2023

@author: david

LeetCode - Easy 1844. Replace All Digits with Characters


Runtime
49ms
Beats 41.65%of users with Python3

Memory
16.27mb
Beats 69.57%of users with Python3
"""

class Solution:
    def replaceDigits(self, s: str) -> str:
            
        def shift(letter: str, n: int):
            return chr( ord(letter) + n )

        L = list(s)

        for i in range(len(L)):
            if i%2 == 1:
                L[i] = shift(L[i-1], int(L[i]))
        
        return ''.join(L)
