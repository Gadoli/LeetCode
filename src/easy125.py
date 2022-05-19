# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 23:33:11 2022

@author: david

LeetCode - 125. Valid Palindrome
"""


def isPalindrome(s):
    getVals = list([val for val in s if val.isalnum()])
    result = "".join(getVals)
    result = result.lower()
    mid = len(result)//2
    half_one = result[:mid]
    if len(result)%2==0:
        half_two = result[mid:]
    else:
        half_two = result[mid+1:]
    
    return half_one == half_two[::-1]
        