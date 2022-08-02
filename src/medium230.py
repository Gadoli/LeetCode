# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 22:51:19 2022

@author: david

LeetCode - Medium 230. Kth Smallest Element in a BST
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



"""
Runtime: 107 ms, faster than 13.44% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18 MB, less than 89.14% of Python3 online submissions for Kth Smallest Element in a BST.
"""
# my first solution
def recur(root, L):
    if not root: return
    
    L.append(root.val)
    recur(root.left,L)
    recur(root.right,L)
    
    return
    
def kthSmallest(root,k):
    L = []
    recur(root,L)
    return sorted(L)[k-1]




"""
Runtime: 74 ms, faster than 62.18% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.1 MB, less than 45.03% of Python3 online submissions for Kth Smallest Element in a BST.
"""
# my second solution
# from last month
def levelOrder(root):
    if not root: return []

    L = [root.val]
    level = [root]

    while len(level) > 0:
        tmp = []
        for i in level:
            if i.left: tmp.append(i.left)
            if i.right: tmp.append(i.right)    
        level = tmp
        
        if level == []: return L
        
        L += [k.val for k in level]
        
    return L    
    

def kthSmallest2(root, k):
    L = levelOrder(root)
    return sorted(L)[k-1]