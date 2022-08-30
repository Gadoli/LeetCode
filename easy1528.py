# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 17:29:36 2022

@author: david

Idea :
    1 - create a temporary list  of length len(s)
    2 - modify according indices and s

LeetCode - Easy 1528. Shuffle String
"""

def restoreString(s, indices):
    L = ['a']*len(s)
    cpt = 0
    for i in indices:
        L[i] = s[cpt]
        cpt += 1
    return "".join(L)