# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:45:46 2022

@author: david

LeetCode - Easy 1678. Goal Parser Interpretation
"""

def interpret(command):
    S = command.replace("()","o")
    return S.replace("(al)", "al")