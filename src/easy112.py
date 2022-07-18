# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:05:12 2022

@author: david

LeetCode - Easy. 112. Path Sum
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def pathSum(root, targetSum, total, res):
    if not root: return res[0]
    
    if not root.left and not root.right:
        if not res[0]:
            res[0] = (targetSum == total + root.val)
            return res[0]
            
    if root.left: pathSum(root.left, targetSum, total+root.val, res)
    if root.right: pathSum(root.right, targetSum, total+root.val, res)
        
    return res[0]

def hasPathSum(root, targetSum):
    return pathSum(root, targetSum, 0, [False])