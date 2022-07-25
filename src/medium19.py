# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 19:01:13 2022

@author: David

LeetCode - Medium 19. Remove Nth Node From End of List
"""
# my solution
def firstTry(head, n):
    # getting the length of the linked list
    tmp = head
    L = []
    cpt = 0
    while tmp:
        L.append
        tmp = tmp.next
        cpt += 1
        
    if cpt==1: return None
    
    # case where it's the first element
    start = cpt - n
    if start == 0: return head.next
    
    # case where it's the last element
    if n == 1:
        tmp = head
        k = 0
        while head:
            if k == start-1:
                head.next = None
                return tmp
            head = head.next
            k += 1
        return tmp
    
    # other cases
    tmp = head
    end = n - 1
    for i in range(cpt):
        if start-1==i:
            head.next = head.next.next
            return tmp
        head = head.next
            
    return tmp


def removeNthFromEnd(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    
    # case where it's the first element
    if not fast:
        return head.next
    
    # will loop (len(linkedlist) - n) times
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head