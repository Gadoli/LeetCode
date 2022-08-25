# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:45:49 2022

@author: david

LeetCode - 2236. Root Equals Sum of Children
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkTree(root):
    return root.left.val + root.right.val == root.val