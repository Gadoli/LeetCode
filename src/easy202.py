# -*- coding: utf-8 -*-
"""
Created on Wed May 18 17:36:57 2022

@author: david

LeetCode - Easy 202. Happy Number
"""

def isHappy(n):
    res = n
    S = set()
    while res != 1:
        if res in S:
            return False
        S.add(res)
        res = list(str(res))
        tmp = 0
        for i in res:
            tmp += pow(int(i),2)
        res = tmp
    return True