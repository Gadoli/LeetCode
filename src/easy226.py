# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:43:12 2022

@author: David

LeetCode - Easy 226. Invert Binary Tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def recur(root):
    if not root: return root

    root.left, root.right = root.right, root.left
        
    if root.left: invertTree(root.left)
    if root.right: invertTree(root.right)
    return root
        
def invertTree(root):
    return recur(root)