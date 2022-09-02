# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 23:32:35 2022

@author: david

LeetCode - 1816. Truncate Sentence
"""

def truncateSentence(s, k):
    return " ".join(s.split()[:k])