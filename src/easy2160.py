# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:01:27 2022

@author: david

LeetCode - 2160. Minimum Sum of Four Digit Number After Splitting Digits
"""

def minimumSum(num):
    L = list(str(num))
    a = int(min(L) + max(L))
    L.remove(min(L))
    L.remove(max(L))
    return a + int(min(L) + max(L))