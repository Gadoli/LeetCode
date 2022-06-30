# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:12:12 2022

@author: david

LeetCode - Easy 206. Reverse Linked List
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if not head: return None
    
    L = []
    
    # seems like I'm cheating over here
    while head:
        L.append(head.val)
        head = head.next
    
    tmp2 = ListNode(L[0])
    for i in range(1,len(L)):
        tmp1 = ListNode(L[i])
        tmp1.next = tmp2
        tmp2 = tmp1
    return tmp2
            
            