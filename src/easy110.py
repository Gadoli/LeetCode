# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:51:01 2022

@author: David

LeetCode - Easy 110. Balanced Binary Tree

Runtime: 61 ms, faster than 82.66% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.9 MB, less than 11.68% of Python3 online submissions for Balanced Binary Tree.
"""

# my solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recur(root, n):
    # if went to an empty node, substract 1 since it's not a node
    # (parent node is not a leaf)
    if not root: return n-1
    
    # a leaf has been reached
    if not root.left and not root.right: return n
    

    # temporary variables, using a and b multiple times
    # adding +1 since we're going deeper in the tree
    # adding from top to bottom
    a = recur(root.left, n+1)      # height of left subtree
    b = recur(root.right, n+1)     # height of right subtree
    
    # if one of a or b is at least False, i.e. tree is not a h-b BT
    if not a or not b: return False
    
    # by function's construct a and b are int
    # h-b BT definition can be check
    if abs(a-b)<=1: return max(a,b)
    # def is not verified
    return False        
    
    
    
def isBalanced(root):
    # empty tree
    if not root: return True
    
    # if BT is h-b, result will be an int
    # starting at 1, easier for cases [a], [a,b]
    if recur(root,1): return True
    return False








# from discussion - commented and understood
class Solution(object):
    def isBalanced(self, root):
            
        def check(root):
            # when an empty node has been reached
            if root is None:
                return 0
            
            # getting height of left and right subtrees
            left  = check(root.left)
            right = check(root.right)
            
            # if one of the subtrees are not a h-b BT
            # or left and right subtrees cannot be part of a h-b BT
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            # adding height from bottom to top
            # e.g. with the BT [1,2,3,4] and recuring check going only left :
            # root (1) -> left (2) -> left (4) -> left (None)
            # ~> their respective values are ~> 3 2 1 0
            # having +1 with the actual height doesn't matter here
            return 1 + max(left, right)
            
        return check(root) != -1
