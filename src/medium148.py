# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:04:05 2022

@author: David

LeetCode - Medium 148. Sort List
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first solution
# =============================================================================
# Runtime: 748 ms, faster than 66.96% of Python3 online submissions for Sort List.
# Memory Usage: 36.5 MB, less than 54.39% of Python3 online submissions for Sort List.
# =============================================================================
# cheating a bit
def sortList(head):
    # case when linked list is empty
    if not head: return head
    
    # transforming linked list to a list and sorting it
    L = []
    tmp = head
    while head:
        L.append(head.val)
        head = head.next
    L.sort()
    
    # transforming the sorted list into a linked list
    res = tmp
    for i in range(len(L)-1):
        tmp.val = L[i]
        tmp.next = ListNode()
        tmp = tmp.next
    tmp.val = L[-1]
    return res

# from discussion, commented for comprehension
def merge(h1, h2):
    dummy = tail = ListNode(None)
    # going through each head
    while h1 and h2:
        # comparing their value
        # build tail and update accordingly
        if h1.val < h2.val:
            tail.next, tail, h1 = h1, h1, h1.next
        else:
            tail.next, tail, h2 = h2, h2, h2.next
    
    # add the last element
    tail.next = h1 or h2
    # dummy is tail at the beginning which is an empty ListNode
    return dummy.next

def sortList2(head):
    # if linked list is empty or size 1
    if not head or not head.next: return head
    
    # pre will permit to cut the linked list at the middle
    # fast will permit to determine the linked list's middle
    # slow will start at the linked list's middle
    pre, slow, fast = None, head, head
    while fast and fast.next:
        pre, slow, fast = slow, slow.next, fast.next.next
    # cutting properly
    pre.next = None
    
    # recursively dividing the linked list, sort and merge them afterwards
    return merge(*map(sortList2, (head, slow)))