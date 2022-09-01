# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:45:51 2022

@author: david

Idea :
    1 - go through each ListNode, add and carry accordingly 
    2 - add the remaining ListNode taking into account the carry

LeetCode - Medium 2. Add Two Numbers
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# use to properly add the carry when doing addition
def checkcarry(carry, R):
    if carry:
        if carry>9:
            R.next = ListNode(0)
            R.next.next = ListNode(1)
        else:
            R.next = ListNode(carry)

# to avoid code repetition
# will add accordingly the remainging ListNode
def tempo(l, R, carry):
    while l:
        num = l.val + carry
        R.val = num%10
        carry = num//10
        l = l.next
        if l:
            R.next = ListNode()
            R = R.next
    checkcarry(carry, R)


def addTwoNumbers(l1, l2):
    R = ListNode()
    tmp = R
    carry = 0
    
    while l1 and l2:
        num = l1.val + l2.val + carry
        if num>9 :
            R.val = num%10
            carry = num//10
        else:
            R.val = num
            carry = 0
        l1 = l1.next
        l2 = l2.next
        if l1 and l2:
            R.next = ListNode()
            R = R.next
    
    if not l1 and not l2:
        checkcarry(carry, R)
        return tmp
    
    R.next = ListNode()
    R = R.next
    if l1:
        tempo(l1, R, carry)
    if l2:
        tempo(l2, R, carry)
    
    return tmp







# from accepted solutions - NOT understood yet
f = open("user.out", "w")
lines = __Utils__().read_lines()
trash = {91: None, 93: None, 44: None, 10: None}
while True:
    try:
        param_1 = int(next(lines).translate(trash)[::-1])
        param_2 = int(next(lines).translate(trash)[::-1])
        f.writelines(("[", ",".join(str(param_1 + param_2))[::-1], "]\n"))
    except StopIteration: exit()








# -*- coding: utf-8 -*-
"""
Previous version from long time ago

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
def addTwoNumbers2(l1: [], l2: []) -> []:
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