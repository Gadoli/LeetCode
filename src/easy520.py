# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:32:17 2022

@author: david

LeetCode - Easy 520. Detect Capital
"""

from string import ascii_uppercase as A_U
from string import ascii_lowercase as a_l

def detectCapitalUse(word):
    # tmp value to check at the end
    AllCap = True
    AllLow = True
    Cap = True
    
    # updating variables if needed
    for c in word:
        if c not in A_U: AllCap = False
        if c not in a_l: AllLow = False
    if word[0] in A_U:
        for c in word[1:]:
            if c not in a_l: Cap = False
    else: Cap = False
    
    return AllCap or AllLow or Cap