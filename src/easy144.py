# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:13:38 2022

@author: david

LeetCode - Easy 144. Binary Tree Preorder Traversal

Runtime: 41 ms, faster than 70.85% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.9 MB, less than 13.06% of Python3 online submissions for Binary Tree Preorder Traversal.
"""

def preorderTraversal(root):
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right) if root else []