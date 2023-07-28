# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:52:14 2023

@author: david

LeetCode - Easy 2325. Decode the Message

Runtime
51ms
Beats 56.34%of users with Python3

Memory
16.24mb
Beats 90.03%of users with Python3
"""

import string

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = list(string.ascii_lowercase)
        L = sorted(set(key), key=key.index)
        if " " in L: L.remove(" ")
        for i in range(len(L[:26])):
            alphabet[i] = L[i]

        R = []
        alphabet = list(string.ascii_lowercase)
        for s in message:
            if s == " ":
                R.append(s)
            else:
                R.append(alphabet[L.index(s)])

        return "".join(R)