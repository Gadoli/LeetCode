# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:19:16 2023

@author: david

LeetCode - Easy 1773. Count Items Matching a Rule

Runtime
270ms
Beats 84.30%of users with Python3

Memory
22.52mb
Beats 75.93%of users with Python3
"""

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type": index = 0
        if ruleKey == "color": index = 1
        if ruleKey == "name": index = 2
        cpt = 0
        for item in items:
            if item[index] == ruleValue:
                cpt+=1
        return cpt