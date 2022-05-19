# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:26:52 2022

@author: david

LeetCode - Medium 46. Permutations
LeetCode - Medium 47. Permutations II

ff afeter multiple try
should've added function beforehand to handle res
"""

def permute(nums):
    R = []
    recur(nums, [], R)
    return R

def recur(nums, L, R):
    if not nums:
        R.append(L)
    
    for i in range(len(nums)):
        recur(nums[:i]+nums[i+1:], L+[nums[i]], R)
        
def permuteUnique(nums):
    R = permute(nums)
    S = set()
    for L in R:
        tmp = ""
        for i in L:
            tmp += str(i)
        S.add(tmp)
    M = [list(j) for j in S]
    res = []
    
    minus = False
    for L in M:
        tmp = []
        print(L)
        for k in L:
            if k=='-':
                minus = True
            elif minus:
                tmp.append(int(k)*-1)
                minus = False
            else:
                tmp.append(int(k))
        res.append(tmp)
    return res
        