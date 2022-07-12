# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 21:09:26 2022

@author: david

LeetCode - Medium 62. Unique Paths
dynamic programming

Runtime: 41 ms, faster than 71.59% of Python3 online submissions for Unique Paths.
Memory Usage: 13.9 MB, less than 73.42% of Python3 online submissions for Unique Paths.
"""

def uniquePaths(m, n):
    # time-complexity and space complexity : O(m*n)
    # best solution mathematical one : C(m+n-2,n-1)
    
    grid = []
    for k in range(m): 
        grid.append([0]*n)
    
    for i in range(0,m):
        for j in range(0,n):
            if i>=1 and j>=1:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
            if i==0 or j==0:
                grid[i][j] = 1
    
    return grid[m-1][n-1]