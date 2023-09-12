# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:23:02 2023

@author: david

LeetCode - Easy 2810. Faulty Keyboard

Runtime
47ms
Beats 71.35%of users with Python3

Memory
16.27MB
Beats 70.63%of users with Python3
"""

class Solution:
    def finalString(self, s: str) -> str:
        L = []
        for c in s:
            if c=="i":
                L = L[::-1]
            else:
                L.append(c)

        return "".join(L)