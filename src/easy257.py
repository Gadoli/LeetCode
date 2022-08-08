# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 23:09:19 2022

@author: david

LeetCode - Easy 257. Binary Tree Paths
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getRootToLeaf(root, H, R):
    # adding root value in string format in history
    H.append(str(root.val))
    
    # a leaf has been reached - add History to Res
    if not root.left and not root.right: R.append(H)
    
    # recurring on both sides if possible - make sure to copy lists
    if root.left: getRootToLeaf(root.left, H.copy(), R)
    if root.right: getRootToLeaf(root.right, H.copy(), R)
        
        
def binaryTreePaths(root):
    # getting all root-to-leaf paths
    R = []
    getRootToLeaf(root,[],R)
    
    # creating the correct output format
    M  = []
    for hist in R:
        tmp = [val for val in hist]
        M.append("->".join(tmp))
    return M