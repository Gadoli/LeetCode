# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:15:53 2022

@author: david

LeetCode Easy 145. Binary Tree Postorder Traversal

Runtime: 35 ms, faster than 85.76% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.9 MB, less than 13.25% of Python3 online submissions for Binary Tree Postorder Traversal.
"""

def postorderTraversal(root):
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val] if root else []