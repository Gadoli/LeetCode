# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:20:52 2022

@author: david

LeetCode - Easy - 1281. Subtract the Product and Sum of Digits of an Integer
"""

def subtractProductAndSum(n):
    L = [int(i) for i in list(str(n))]
    return math.prod(L) - sum(L)