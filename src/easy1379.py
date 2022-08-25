# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:45:20 2022

@author: david

LeetCode - Easy 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getTargetCopy(original, cloned, target):
    def recur(root, target, R):
        if root.val == target.val: R.append(root)

        if root.left: recur(root.left, target, R)
        if root.right: recur(root.right, target, R)
    
    L = []
    recur(cloned, target, L)
    return L[0]