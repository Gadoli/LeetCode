# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:55:27 2024

@author: david

LeetCode - Easy 1502. Can Make Arithmetic Progression From Sequence
"""

from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr)==2:
            return True
        
        arr.sort()
        diff = abs(arr[0]-arr[1])
        for i in range(1, len(arr)-1):
            if diff != abs(arr[i] - arr[i+1]):
                return False
        return True