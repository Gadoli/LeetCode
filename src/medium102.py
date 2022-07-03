# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 18:04:12 2022

@author: david

LeetCode - Medium 102. Binary Tree Level Order Traversal

Runtime: 39 ms, faster than 85.60% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.1 MB, less than 98.94% of Python3 online submissions for Binary Tree Level Order Traversal.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
def levelOrder(root):
    if not root: return []

    L = [[root.val]]
    level = [root]

    while len(level) > 0:
        tmp = []
        for i in level:
            if i.left: tmp.append(i.left)
            if i.right: tmp.append(i.right)    
        level = tmp
        
        if level == []: return L
        
        L.append([k.val for k in level])
        
    return L 