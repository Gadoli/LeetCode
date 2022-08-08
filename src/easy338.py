# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 22:49:14 2022

@author: david

LeetCode - Easy 338. Counting Bits

Runtime: 116 ms, faster than 73.77% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 78.97% of Python3 online submissions for Counting Bits.
"""

def countBits(n):
    # for each int from 0 to n
    # transform it to a binary format then count the number of 1
    # using a comprehension
    return [bin(i).count("1") for i in range(n+1)]