# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:43:02 2022

@author: david

LeetCode - Easy 2114. Maximum Number of Words Found in Sentences

Idea : 
    1 - split each sentences by spaces and get the length
    2 - return the max length
"""

def mostWordsFound(sentences):
    return max(len(s.split(" ")) for s in sentences)