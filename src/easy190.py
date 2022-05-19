# -*- coding: utf-8 -*-
"""
Created on Tue May 17 20:08:02 2022

@author: david

LeetCode - Easy 190. Reverse Bits
"""

def reverseBits(n):
    L = list(str(int(n)))[::-1]
    res = 0
    for i in range(len(L)):
        res += int(L[i])*pow(10,len(L) - i)
    return int(str(res),2)