# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 20:05:54 2022

@author: David

LeetCode - Easy 234. Palindrome Linked List
"""

# not fast- check discussion
def isPalindrome(head):
    L = []
    while head:
        L.append(head.val)
        head = head.next
    n = len(L)
    if n%2==1: return L[:n//2 + 1] == L[n//2:][::-1]
    return L[:n//2] == L[n//2:][::-1]