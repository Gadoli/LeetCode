# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 11:04:56 2022

@author: david
"""
# =============================================================================
# Wrong cause didn't use singly-linked list FTM
# =============================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(l1: [], l2: []) -> []:
    lengthl1 = len(l1)
    lengthl2 = len(l2)
    minLength = min(lengthl1, lengthl2)
    maxLength = max(lengthl1, lengthl2)
    L = []
    tmp2 = 0
    for i in range(minLength):
        tmp = l1[i] + l2[i] + tmp2
        L.append(tmp%10)
        tmp2 = int(tmp/10)
    
    if lengthl1==lengthl2:
        return L
    
    if lengthl1>lengthl2:
        for j in range(minLength,maxLength):
            L.append(l1[j])
        return L
    
    for j in range(minLength,maxLength):
        L.append(l2[j])
    return L
    
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
print(addTwoNumbers([2,4,3],[5,6,4]))

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
print(addTwoNumbers([0],[0]))


# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))