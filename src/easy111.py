# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 22:54:00 2022

@author: david

LeetCode - Easy 111. Minimum Depth of Binary Tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def recur(root, R, n):
    if not root.left and not root.right:
        R.append(n)
        return
    
    if root.left: recur(root.left, R, n+1)
    if root.right: recur (root.right, R, n+1)
    
    return

def minDepth(root):
    if not root: return 0
    R = []
    recur(root, R, 1)
    return min(R)