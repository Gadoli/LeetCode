# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:00:34 2023

@author: david

LeetCode - Easy 1791. Find Center of Star Graph

Runtime
774ms
Beats 99.88%of users with Python3

Memory
52.32mb
Beats 13.74%of users with Python3
"""

from typing import List

from itertools import chain
from collections import Counter


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return Counter(list(chain(*edges))).most_common(1)[0][0]