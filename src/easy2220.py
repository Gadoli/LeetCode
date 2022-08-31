# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 19:12:43 2022

@author: david

LeetCode - Easy 2220. Minimum Bit Flips to Convert Number
"""

def minBitFlips(start, goal):
    # transform to binary, reading from left to right
    S = list(bin(start)[2:][::-1])
    G = list(bin(goal)[2:][::-1])
    
    len_S = len(S)
    len_G = len(G)
    
    # adjusting size
    if len_S<len_G:
        S += ['0']*(len_G - len_S)
    else:
        G += ['0']*(len_S - len_G)
    
    # compute difference
    return sum(1 for a, b in zip(S, G) if a != b)