# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:25:51 2022

@author: david

LeetCode - Easy 2011. Final Value of Variable After Performing Operations
"""

def finalValueAfterOperations(operations):
        c = 0
        for op in operations:
            if "+" in op: 
                c += 1
                continue
            if "-" in op: 
                c -= 1
                continue
        return c