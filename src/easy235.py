# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 17:38:07 2022

@author: david

LeetCode - Easy 235. Lowest Common Ancestor of a Binary Search Tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def history(self, root, H, target):
        if root is None:
            return False
        
        if self.history(root.left, H, target):
            H.append(root)
            return True

        if self.history(root.right, H, target):
            H.append(root)
            return True

        if root.val == target.val: 
            H.append(root)
            return True

        return False
    
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        H = []
        self.history(root, H, p)
        
        L = []
        self.history(root, L, q)
        
        for i in range(len(L)):
            for k in range(len(H)):
                if L[i] == H[k]:
                    return L[i]
        
        return None