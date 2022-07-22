# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:09:34 2022

@author: david

LeetCode - Medium 692. Top K Frequent Words
"""

from collections import Counter

def topKFrequent(words, k):
    C = Counter(words)
    D = C.most_common()
    tmp = D[0][1]
    L_tmp = []
    R = []
    for key,v in D:
        if v==tmp: L_tmp.append(key)
        else:
            R = R + sorted(L_tmp)
            tmp = v 
            L_tmp = [key]
    if L_tmp:
        R = R + sorted(L_tmp)
    return R[:k]