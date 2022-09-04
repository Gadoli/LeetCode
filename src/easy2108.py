# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:13:40 2022

@author: david

LeetCode - Easy 2108. Find First Palindromic String in the Array
"""



# solution ! 
def firstPalindrome(words):
    for i in words:
        if i == i[::-1]:
            return i
    return ""


# 1st solution
def firstPalindrome2(words):
    for word in words:
        mid = len(word)//2
        half_one = word[:mid]
        if len(word)%2==0:
            half_two = word[mid:]
        else:
            half_two = word[mid+1:]

        if half_one == half_two[::-1]:
            return word
    return ""