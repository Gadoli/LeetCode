# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 18:09:48 2022

@author: david

LeetCode - Easy 21. Merge Two Sorted Lists

# not the best see other submissions from months ago
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(list1, list2):
    resList = ListNode()
    
    if list1.val < list2.val :
        resList.val = list1.val 
        list1 = list1.next
        
    else:
        resList.val = list2.val 
        list1 = list2.next
    
    while list1 or list2:
        if list1.val < list2.val :
            resList.next = list1.next 
            resList = list1.next
            list1 = list1.next 
        
        else:
            resList.next = list2.next 
            resList = list2.next
            list2 = list2.next 
            
        return resList