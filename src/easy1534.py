# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:48:18 2023

@author: david

LeetCode - Easy 1534. Count Good Triplets
"""

from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cpt = 0

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):

                    if not 0 <= i < j < k < len(arr):
                        continue
                    if not abs(arr[i] - arr[j]) <= a:
                        continue
                    if not abs(arr[j] - arr[k]) <= b:
                        continue
                    if not abs(arr[i] - arr[k]) <= c:
                        continue
                    cpt += 1
                    
        return cpt     