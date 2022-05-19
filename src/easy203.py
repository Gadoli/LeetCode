# -*- coding: utf-8 -*-
"""
Created on Wed May 18 17:52:57 2022

@author: david

LeetCode - Easy 203. Remove Linked List Elements
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    head_tmp = head
    tmp = None
    if head is None:
        return None
    while head.next:
        if head.val == val:
            if tmp:
                tmp.next = head.next
            else:
                head_tmp = head.next
        else:
            tmp = head
        head = head.next
    if head.val == val:
        if tmp:
            tmp.next = None
        else:
            return None
    return head_tmp
        
        