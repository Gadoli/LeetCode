# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:26:20 2023

@author: david

LeetCode - Easy 1656. Design an Ordered Stream

"""

from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.L = [""] * n
        self.i = 0


    def insert(self, idKey: int, value: str) -> List[str]:
        self.L[idKey-1] = value
        
        tmp = []

        while self.i < len(self.L) and self.L[self.i] != "" :
            tmp.append(self.L[self.i])
            self.i += 1

        return tmp


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)