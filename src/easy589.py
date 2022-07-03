# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 17:43:34 2022

@author: david

LeetCode - Easy 589. N-ary Tree Preorder Traversal
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
        
def dfs(root, L):
    if not root: return L
    
    L.append(root.val)
    
    if not root.children: return L
    
    for i in root.children:
        dfs(i,L)
    return L
        
def preorder(root):
    return dfs(root,[])