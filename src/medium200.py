# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:41:43 2022

@author: david

LeetCode - Medium 200. Number of Islands
"""

class Solution:
    def dfs(self, grid, sr, sc, visited):
        if (sr,sc) in visited: return False
        visited.add((sr,sc))
        if grid[sr][sc] == "0": return False
        
        if sr > 0: self.dfs(grid, sr-1, sc, visited)
        if sr < len(grid) - 1: self.dfs(grid, sr+1, sc, visited)
        if sc > 0: self.dfs(grid, sr, sc-1, visited)
        if sc < len(grid[0]) - 1: self.dfs(grid, sr, sc+1, visited)
                    
        return True
    
    def numIslands(self, grid):
        visited = set()
        cpt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited: continue
                if self.dfs(grid, i, j, visited):
                    cpt += 1
        return cpt
