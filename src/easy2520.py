# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:24:00 2023

@author: david

LeetCode - Easy 2520. Count the Digits That Divide a Number

Runtime
33ms
Beats 98.42%of users with Python3

Memory
16.28mb
Beats 62.11%of users with Python3
"""

class Solution:
    def countDigits(self, num: int) -> int:
        cpt = 0
        for n in str(num):
            if num%int(n)==0:
                cpt+=1
        return cpt