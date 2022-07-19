# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:54:20 2022

@author: david

LeetCode - Easy 844. Backspace String Compare
"""

def removeFrontSpace(s):
    cpt_s = 0
    i = 0
    while i < len(s):
        if s[i] == '#':
            cpt_s += 1
            s.pop(i)
            continue
        if cpt_s >0:
            s.pop(i)
            cpt_s -= 1
            continue
        i += 1
    
def backspaceCompare(s, t):
    S = list(s)[::-1]
    T = list(t)[::-1]
    
    removeFrontSpace(S)
    removeFrontSpace(T)
    
    return S==T