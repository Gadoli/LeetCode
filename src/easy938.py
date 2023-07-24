# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:46:15 2023

@author: david

LeetCode - Easy 938. Range Sum of BST

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def search(root, R):
            if not root: return R[0]

            if low <= root.val and root.val <= high:
                R[0] += root.val

            if not root.left and not root.right: return R[0]

            search(root.left,R)
            search(root.right,R)
            return R[0]

        return search(root, [0])