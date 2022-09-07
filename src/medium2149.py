# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:34:04 2022

@author: david

LeetCode - Medium 2149. Rearrange Array Elements by Sign
"""

def rearrangeArray(nums):
    Pos = []
    Neg = []
    R = []
    for i in nums:
        if i>0: Pos.append(i)
        else: Neg.append(i)
    for i in range(len(Pos)):
        R.append(Pos[i])
        R.append(Neg[i])
    return R