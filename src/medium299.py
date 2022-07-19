# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:01:58 2022

@author: david

LeetCode - Medium. 299. Bulls and Cows
"""

def getHint(secret, guess):
    # counting bulls and creating S and G
    bulls_count = 0
    pop_list = []
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls_count += 1
            pop_list.append(i)
    S = [secret[i] for i in range(len(secret)) if i not in pop_list]
    G = [guess[i] for i in range(len(secret)) if i not in pop_list]
    
    # creating HashMap/Dict of S and G
    Map_S = {}
    Map_G = {}
    for i in range(len(S)):
        if not S[i] in Map_S: Map_S[S[i]] = 1
        else: Map_S[S[i]] += 1
        
        if not G[i] in Map_G: Map_G[G[i]] = 1
        else: Map_G[G[i]] += 1
    
    # counting cows using Map_S and Map_G, no need to update them
    cows_count = 0
    for k in Map_S.keys():
        if k not in Map_G.keys(): continue
        cows_count += min(Map_S[k],Map_G[k])
    
    return f"{bulls_count}A{cows_count}B"