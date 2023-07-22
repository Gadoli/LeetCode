# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 17:25:37 2023

@author: david

LeetCode - Easy 2485. Find the Pivot Integer
"""

# from typing import List

class Solution:
    def pivotInteger(self, n: int) -> int:
        # Mathematical answer 
        x=(n*(n+1)/2)**0.5
        if x == int(x):
            return int(x)
        else:
            return -1
        
        # first solution
        """
        if n ==1:
            return 1

        L = list(range(1,n+1))
        p = len(L)//2

        def dich(L: List[int], p: int, H: List[int]) -> int:

            if sum(L[:p]) == sum(L[p-1:]):
                return p

            elif sum(L[:p]) < sum(L[p-1:]):
                n = (p+1 + len(L)) // 2
            elif sum(L[:p]) > sum(L[p-1:]):
                n = (p-1) // 2
            
            if n in H:
                return -1
            
            H.append(n)
            return dich(L, n, H)

        return dich(L, p, [p])
        """

        