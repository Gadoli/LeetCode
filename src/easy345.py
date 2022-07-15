# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:32:49 2022

@author: david

LeetCode - Easy 345. Reverse Vowels of a String
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        # Time complexity O(len(s)) , Memory complexity : O(len(s))
        
        # initializing
        voyels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        L = list(s)
        
        # getting all voyels in order and reversing them
        R = []
        for c in L:
            if c in voyels:
                R.append(c)
        R.reverse()
        
        # update voyels
        for i in range(len(L)):
            if L[i] in voyels:
                L[i] = R.pop(0)
        
        return "".join(L)