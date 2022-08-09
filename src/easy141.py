# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 22:41:52 2022

@author: david

LeetCode - Easy 141. Linked List Cycle

Runtime: 62 ms, faster than 86.53% of Python3 online submissions for Linked List Cycle.
Memory Usage: 18 MB, less than 10.56% of Python3 online submissions for Linked List Cycle.
"""

def hasCycle(head):
    # creating a set to store seen nodes
        S = set()
        
        # going through each nodes
        while head:
            
            # first time to see this node
            if head not in S:
                S.add(head)
                head = head.next
                
            # node is already in the set i.e. hasCycle
            else: return True
            
        # no nodes go back to a seen node
        return False