# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:08:07 2023

@author: david

LeetCode - Easy 509. Fibonacci Number
"""

import math


# Dynammic programming solution
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0

        dp = [0] *(n+1)
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
    
    
    
# Mathematical solution
class Solution2:
    def fib(self, n: int) -> int:
        phi = (1 + math.sqrt(5))/2
        xhi = 1 - phi
        return int((math.pow(phi, n) - math.pow(xhi, n))/math.sqrt(5))