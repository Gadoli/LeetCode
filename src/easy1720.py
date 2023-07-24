# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:23:24 2023

@author: david

LeetCode - Easy 1720. Decode XORed Array

Runtime
223ms
Beats 86.27%of users with Python3

Memory
18.04mb
Beats 94.47%of users with Python3
"""

from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        L = [first]
        for n in encoded:
            tmp = L[-1] ^ n
            L.append(tmp)
        return L
