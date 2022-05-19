# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:06:04 2022

@author: david

Leetcode - Easy 168. Excel Sheet Column Title
"""

def convertToTitle(columnNumber):
    res = ""
    while columnNumber>26:
        tmp = columnNumber%26
        columnNumber = columnNumber//26
        if tmp == 0:
            res += 'Z'
            columnNumber -= 1
            continue
        res += chr(tmp + 64) # 65 being A, but we start at 1
    res += chr(columnNumber + 64)
    return res[::-1]