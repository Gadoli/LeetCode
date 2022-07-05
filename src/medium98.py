# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:29:40 2022

@author: david

LeetCode - Medium 98. Validate Binary Search Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Soolution:
    def inorder(self, root, output):
        if root is None:
            return
        
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
    
    def isValidBST(self, root):
        L = []
        self.inorder(root,L)
        for i in range(1,len(L)):
            if L[i-1] >= L[i]: return False
        return True
            