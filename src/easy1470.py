# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:40:02 2022

@author: david

LeetCode - Easy 1470. Shuffle the Array
"""

def shuffle(nums, n):
        L = []
        A = nums[:n]
        B = nums[n:]
        for i in range(n):
            L.append(A[i])
            L.append(B[i])
        return L