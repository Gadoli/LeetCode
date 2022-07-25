# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:42:37 2022

@author: David

LeetCode - Medium 328. Odd Even Linked List

Runtime: 54 ms, faster than 76.13% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 16.6 MB, less than 77.11% of Python3 online submissions for Odd Even Linked List.
"""

def oddEvenList(head):
    # case when head is empty    
    if not head: return head
    
    # linkedlist named according to the group indices
    odd, even = head, head.next
    # res and mid for memory purposes
    res, mid = odd, even
    
    # continue if we can still get next incides
    while odd.next and even.next:
        # doing so avoids us to use temporary variables
        odd.next, odd = odd.next.next, odd.next.next
        even.next, even = even.next.next, even.next.next
    
    # connect odd's end and even's start
    odd.next = mid
    return res