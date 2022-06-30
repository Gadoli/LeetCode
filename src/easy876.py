# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:16:34 2022

@author: david

LeetCode - Easy 876. Middle of the Linked List
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def middleNode(head):
    tmp = head
    cpt = 0

    while tmp:
        tmp = tmp.next
        cpt +=1
    
    for i in range(round(cpt//2 + 0.1)):
        head = head.next
    return head