# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:05:11 2022

@author: david

LeetCode - Easy 409. Longest Palindrome
"""

def longestPalindrome(s):
    
    # dict part could have been replaced with collections.Counter(s).itervalues():
    D = dict()
    
    # counting occurrence of each letters
    for i in s:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    
    maxOdd = 0
    cpt = 0
    cptOdd = 0
    for v in D.values():
        if v%2 == 0:
            cpt += v
        elif cptOdd < 1:
            cptOdd += 1
            maxOdd = max(maxOdd, v)
        elif v-1 > 0:
            cpt += v-1
    cpt += maxOdd
    return cpt
    
        
    