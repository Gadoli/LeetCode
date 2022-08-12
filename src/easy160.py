# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 18:24:03 2022

@author: david

LeetCode - Easy 160. Intersection of Two Linked Lists

Runtime: 197 ms, faster than 73.26% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 30.2 MB, less than 12.53% of Python3 online submissions for Intersection of Two Linked Lists.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    # creating temporary variable
    set_A = set()
    
    # adding all nodes of A into a set
    while headA:
        set_A.add(headA)
        headA = headA.next
    
    # for each node in B - check if it's in the set (O(1))
    # i.e. tehre's an intersection between A and B
    while headB:
        if headB in set_A:
            return headB
        headB = headB.next
        
    return None