# -*- coding: utf-8 -*-
"""
Created on Wed May 11 18:11:49 2022

@author: david

LeetCode - Medium 1641. Count Sorted Vowel Strings
"""

def countVowelStrings(n):
    return 0


def recur(n,k):
    R=  0
    if n == 1:
        return k
    for i in range(k):
        R += recur(n-1,k-i)
    return R