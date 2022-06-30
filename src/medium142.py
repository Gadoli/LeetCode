# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:23:45 2022

@author: david

LeetCode - Medium 142. Linked List Cycle II
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def detectCycle(head):
    if not head: return None
    
    # with memory being the size of the List
    # not sure if sets can be used
    S = set()
    
    while head:
        if head in S:
            return head
        S.add(head)
        head = head.next
    
    return None