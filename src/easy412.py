# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:59:26 2022

@author: david

LeetCode - Easy 412. Fizz Buzz

Runtime: 61 ms, faster than 59.91% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15 MB, less than 43.18% of Python3 online submissions for Fizz Buzz.
"""

def fizzBuzz(n):
    L = []
    for i in range(1,n+1):
        if i%3 == 0:
            if i%5 == 0: L.append("FizzBuzz")
            else: L.append("Fizz")
        elif i%5 == 0: L.append("Buzz")
        else: L.append(str(i))
    return L