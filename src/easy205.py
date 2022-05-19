# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:17:31 2022

@author: david

LeetCode - Easy 205. Isomorphic Strings
"""
# not the best version

def oneWay(s, t):
    dict_replace = dict()

    for i in range(len(s)):
        if s[i] != t[i]:
            dict_replace[s[i]] = t[i]

    tmp = t+''
    for i in range(len(s)):
        if s[i] in dict_replace:
            tmp = tmp[:i] + dict_replace[s[i]]  + tmp[i+1:]

    return tmp == t

def isIsomorphic(s, t) -> :
    return oneWay(s,t) and oneWay(t,s)