# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:35:10 2022

@author: david

LeetCode - Easy 169. Majority Element
"""



def majorityElement(nums):
    number = sum(nums)/len(nums)
    D = {}
    for i in nums:
        if number > 0 and abs(i - number) > number:
            continue
        elif number <= 0 and abs(i + number) < number:
            continue
        if i in D:
            D[i] +=1
        else:
            D[i] = 1
    return max(D, key=D.get)
        

