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

# from discussion
def isPalindrome2(head):
    # rev will contain the first half reversed
    rev = None
    
    # fast permits to loop only half's length of the linkedlist
    # slow will be positionned at half pos
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    
    # fast is at the end, length is odd
    if fast: slow = slow.next
    
    # checking if <- (rev) and -> (slow) are equals
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    
    # rev will be empty at the end's loop
    return not rev
