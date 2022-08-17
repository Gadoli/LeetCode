# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:33:36 2022

@author: david

LeetCode - 804. Unique Morse Code Words

Idea : 
    1 - transform all words into its morse code concatenation (transformation)
    2 - add all these transformation in a set
    3 - return the length of the set
"""

# first solution 
"""
Runtime: 48 ms, faster than 67.93% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 13.9 MB, less than 75.48% of Python3 online submissions for Unique Morse Code Words.
"""
def transformStringToMorse(words):
    morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    S = set()
    for w in words:
        S.add("".join([morseAlphabet[ord(c) - 97] for c in w]))
    return S

def uniqueMorseRepresentations(words):
    return len(transformStringToMorse(set(words)))



#2 line solution
"""
Runtime: 76 ms, faster than 8.92% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 13.8 MB, less than 75.48% of Python3 online submissions for Unique Morse Code Words.
"""
def uniqueMorseRepresentations2(words):
    morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    return len({("".join([morseAlphabet[ord(c) - ord('a')] for c in w])) for w in set(words)})
