# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:07:31 2023

@author: david

LeetCode - Easy 832. Flipping an Image

Runtime
69ms
Beats 37.98%of users with Python3

Memory
16.35mb
Beats 50.34%of users with Python3
"""

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        L = []

        for P in image:

            tmp = []
            for i in range(len(P)):
                if P[i] == 0:
                    tmp.append(1)
                else:
                    tmp.append(0)
            
            L.append(tmp[::-1])

        return L