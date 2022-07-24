# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:49:37 2022

@author: David

LeetCode - Medium 43. Multiply Strings

Runtime: 45 ms, faster than 83.59% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.8 MB, less than 74.17% of Python3 online submissions for Multiply Strings.
"""

def multiply(num1, num2):
    n = 0
    for i in num1:
        n = n*10 + int(i)
    m = 0
    for j in num2:
        m = m*10 + int(j)
    return str(n*m)