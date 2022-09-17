# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 18:28:53 2022

@author: david

LeetCode - Easy 2351. First Letter to Appear Twice
"""

def repeatedCharacter(s):
    S = set()
    for c in s:
        if c in S: return c
        S.add(c)
    return "0"