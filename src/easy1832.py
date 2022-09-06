# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 23:15:40 2022

@author: david

LeetCode - Easy 1832. Check if the Sentence Is Pangram
"""

from collections import Counter

def checkIfPangram(sentence):
    return Counter("abcdefghijklmnopqrstuvwxyz") <= Counter(sentence)