# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:21:39 2022

@author: David

LeetCode - Medium 1706. Where Will the Ball Fall

Runtime: 347 ms, faster than 41.06% of Python3 online submissions for Where Will the Ball Fall.
Memory Usage: 14.5 MB, less than 32.60% of Python3 online submissions for Where Will the Ball Fall.
"""


# my solution (DFS)
def ballFallsOut(grid, start):
    if not grid:
        return start
    
    if grid[0][start] == 1:
        if start+1 == len(grid[0]): return -1
        if grid[0][start+1] == -1: return -1
        else: return ballFallsOut(grid[1:],start+1)
    
    if grid[0][start] == -1:
        if start-1 < 0: return -1
        if grid[0][start-1] == 1: return -1
        else: return ballFallsOut(grid[1:],start-1)
    
    return -1
            
def findBall(grid):
    L = []
    for i in range(len(grid[0])):
        L.append(ballFallsOut(grid,i))
    return L


# from discussion - iterative
def findBall2(grid):
    m, n = len(grid), len(grid[0])

    def test(i):
        for j in range(m):
            i2 = i + grid[j][i]
            if i2 < 0 or i2 >= n or grid[j][i2] != grid[j][i]:
                return -1
            i = i2
        return i
    return map(test, range(n))
