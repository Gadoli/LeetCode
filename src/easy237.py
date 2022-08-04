# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 23:14:46 2022

@author: David

LeetCode - Easy 237. Delete Node in a Linked List

Runtime: 62 ms, faster than 49.67% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.1 MB, less than 91.44% of Python3 online submissions for Delete Node in a Linked List.
"""
def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    while node and node.next:
        node.val = node.next.val
        if not node.next.next:
            node.val = node.next.val
            node.next = None
        node = node.next
        