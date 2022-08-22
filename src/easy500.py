# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 22:01:36 2022

@author: david

LeetCode - Easy 500. Keyboard Row

Idea :
    pretty straigth forward

Runtime: 46 ms, faster than 53.43% of Python3 online submissions for Keyboard Row.
Memory Usage: 13.8 MB, less than 98.38% of Python3 online submissions for Keyboard Row.
"""

def findWords(words):
    one = "qwertyuiopQWERTYUIOP"
    two = "asdfghjklASDFGHJKL"
    three = "zxcvbnmZXCVBNM"
    
    L = []
    
    for w in words:
        if all(i in one for i in w): L.append(w)
        elif all(i in two for i in w): L.append(w)
        elif all(i in three for i in w): L.append(w)
    
    return L