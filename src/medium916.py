# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 12:21:36 2022

@author: David

LeetCode - Medium 916. Word Subsets
"""


"""
My solution : 
    
 ultimate word : a union of all word in words2
 words2 = ["ab", "abb", "caa"] -> "aabbc" (U)
 
 counting frequency in ultimate word (U)
 "aabbc" -> {a:2, b:2, c:1} = P (ultimate Counter)
 if ultimate word is a subset of word a from words1
 then a is universal 
 
 1. create ultimate Counter (P)
 2. add to result each word in words1 that are a subset of (U)
    i.e. if P is included in Counter(word)
 
 using Counter and the powerful results using operators
"""

from collections import Counter


def wordSubsets(words1, words2):
    # Getting counted frequency for each word in words2
    S = [Counter(i) for i in words2]     
    P = Counter()
    # union of all the Counter and only keeping max values
    for c in S:
        P = P | c   # union:  max(c[x], P[x])
        
    # if more than 10 =\= letters -> impossible
    if len(P)>10: return []
    
    L = []  # result storage
    
    # going through each word in words1
    for a in words1:
        C = Counter(a)  # counting frequency in a
        
        if C >= P:  # inclusion:  C[x] >= P[x]
            L.append(a)
            
    return L



# first idea - not optimize - did not reduce B to a single word
def wordSubsets2(words1, words2):
    # checking if it's impossible to get a universal
    # counting the # of different letters
    S = set().union(*[set(list(i)) for i in words2])
    if len(S)>10: return []
    
    L = []      # result storage
    # getting frequency for each word in words2
    W = [Counter(i) for i in words2]
    
    # going through each word in words1
    for a in words1:
        add = True      # resetting bool
        C = Counter(a)  # counting frequency in a
        
        # going through each counted frequency in words2
        # C2 is the counted frequency of a word b from words2
        for C2 in W:    
            if C > C2:  # b IS a subset of a
                continue
            else:       # b is NOT a subset of a
                add = False
        
        # the word a is universal with words2 !
        if add:
            L.append(a)
    return L


# instance generator
import random
def giveLetter():
    #String
    string = "abcdefghijklmnopqrstuvwxyz"
    # Faster and more efficient
    return random.choice(string)

# S = set(["".join([giveLetter() for i in range(10)]) for i in range(10000)])