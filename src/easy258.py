# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 19:47:45 2022

@author: david

LeetCode - Easy. 258. Add Digits
"""

def addDigits(self, num: int) -> int:
    # transforming num into a list of string digit
    S = str(num)
    
    # if num contains only one digit return it
    if len(S)==1: return num
    
    # recurring with the correct process
    return self.addDigits(sum([int(i) for i in S]))