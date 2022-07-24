# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:37:49 2022

@author: David

LeetCode - Easy 14. Longest Common Prefix
"""


def longestCommonPrefix(strs):
    if (len(strs)==0): return ""
    if (len(strs)==1): return strs[0]
    
    res = ""
    continueStreaks = True
    
    for i in range(0, len(min(strs, key=len))):
        tmp = [word[i] for word in strs]
        if continueStreaks and all(elem == tmp[0] for elem in tmp):
            res += tmp[0]
        else:
            continueStreaks = False
    return res   