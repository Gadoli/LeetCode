# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:50:10 2022

@author: david

LeetCode - Medium 1338. Reduce Array Size to The Half

Idea : 
    1 - get the frequency of each element sorted by most common
    2 - count the number of element needed to be removed in order
        to reach at least half of arr's length

Runtime: 759 ms, faster than 76.49% of Python3 online submissions for Reduce Array Size to The Half.
Memory Usage: 36.3 MB, less than 37.87% of Python3 online submissions for Reduce Array Size to The Half.
"""

from collections import Counter

def minSetSize(arr):
    length = len(arr)
    C = Counter(arr).most_common()
    count = 0
    total = 0
    for ele in C:
        count += 1
        total += ele[1]
        if total >= length//2:
            return count
    return 0