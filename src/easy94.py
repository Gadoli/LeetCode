# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:42:10 2022

@author: david

LeetCode - Easy 94. Binary Tree Inorder Traversal
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorder(self, root, output):
        if root is None:
            return
        
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
    
    def inorderTraversal(self, root):
        L = []
        self.inorder(root,L)
        return L