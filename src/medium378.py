# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:57:56 2022

@author: david

LeetCode - Medium 378. Kth Smallest Element in a Sorted Matrix

Runtime: 324 ms, faster than 43.58% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 19 MB, less than 13.42% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
"""

def kthSmallest(matrix,k):
    # getting all the elements in one big list
    R = []
    for sub in matrix:
        R = R + sub
    # sorting the big list
    R.sort()
    # return by index
    return R[k-1]