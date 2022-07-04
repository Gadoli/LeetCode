# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:47:29 2022

@author: david

LeetCode - Easy 278. First Bad Version

Runtime: 46 ms, faster than 47.05% of Python3 online submissions for First Bad Version.
Memory Usage: 13.8 MB, less than 96.87% of Python3 online submissions for First Bad Version.
"""

# test function 
def isBadVersion(k):
    if k >= 2: return True
    return False

def firstBadVersion(n):
    a = 1
    b = n
    half = b//2
    
    while abs(b-a)>1:
        print(a,b)
        # superior 
        if not isBadVersion(half):
            a = half
            half = (b - half)//2 + half
            
        # inferior    
        else:
            b = half
            half = half - (half - a)//2
            
    if isBadVersion(a): return a
    if isBadVersion(b): return b