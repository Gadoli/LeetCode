# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:31:02 2022

@author: david

LeetCode - Easy 171. Excel Sheet Column Number
"""

def titleToNumber(columnTitle):
    L = list(columnTitle)
    res = 0
    for i in range(len(L)):
        res += (ord(L[i]) - 64)*pow(26,(len(L) - i - 1))
    return res

# =============================================================================
# def convertToTitle(columnNumber):
#     res = ""
#     while columnNumber>26:
#         tmp = columnNumber%26
#         columnNumber = columnNumber//26
#         if tmp == 0:
#             res += 'Z'
#             columnNumber -= 1
#             continue
#         res += chr(tmp + 64) # 65 being A, but we start at 1
#     res += chr(columnNumber + 64)
#     return res[::-1]
# 
# 
# 
# for i in range(1):
#     print(titleToNumber(convertToTitle(2147483647)))
#     
# =============================================================================
