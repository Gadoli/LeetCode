# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 21:46:03 2022

@author: david

LeetCode - Easy 344. Reverse String
"""

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    
    s[:] -> to modify bytes
    """
    s[:] = s[::-1]