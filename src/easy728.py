# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 17:25:06 2022

@author: david

LeetCode - Easy 728. Self Dividing Numbers

Idea :
    1 - have a function that verifies the property
    2 - loop from left to right and add to res the SFD
    
Runtime: 44 ms, faster than 96.97% of Python3 online submissions for Self Dividing Numbers.
Memory Usage: 13.8 MB, less than 98.11% of Python3 online submissions for Self Dividing Numbers.
"""

# my solution
def selfDividingNumbers(left, right):
    
    # checking if num is a self-dividing number
    def dividingNumber(num):
        # mapping is faster than a list comprehension
        for n in map(int, str(num)):
            if n==0 or num%n != 0:  # condition not met
                return False
        return True
    
    # getting all the self-dividing number from left to right
    L = []
    for n in range(left, right+1):
        if dividingNumber(n):
            L.append(n)
        
    return L




# from discussion - understood
def Func(left, right):
    return [x for x in range(left, right+1) if all((i and (x % i==0) for i in map(int, str(x))))]