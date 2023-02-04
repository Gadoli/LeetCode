# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:48:31 2023

@author: david

eetCode - Easy 2535. Difference Between Element Sum and Digit Sum of an Array

Runtime
123 ms
Beats
94.35%

Memory
14.1 MB
Beats
90.78%
"""

class Solution:
    def getSum(self, n: int) -> int:    
        sum = 0
        while (n != 0):
            sum = sum + (n % 10)
            n = n//10
        return sum
    
    def differenceOfSum(self, nums):
        return abs(sum(self.getSum(n) for n in nums) - sum(nums))
        