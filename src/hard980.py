# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:34:44 2022

@author: david

LeetCode - Hard 980. Unique Paths III

Idea : 
 a - found the starting square
 b - count the number of obstacles
 c - get the number of squares to get valid destination (total squares - #obstacles)
    
 recursion :                                            
    from a start position
    go to any direction that hasn't been visited - updates variables/inputs
    check if history's length is equal to 'c', if so add +1 to Result
    
    using set data structure to have O(1) when using "element in data"
    using tuples for positions to be hashable and therefore be able to use set
     (sets can't contain lists since lists are not hashable contrary to tuples)
    
note to self : check BT version from discuss 2 times faster
"""

# clean and 2nd version
"""
Runtime: 92 ms, faster than 56.05% of Python3 online submissions for Unique Paths III.
Memory Usage: 13.9 MB, less than 94.64% of Python3 online submissions for Unique Paths III.
"""
def uniquePathsIII(grid):
    # gird size
    m = len(grid)
    n = len(grid[0])
    
    # internal function to find the starting position and # obstacles
    # N.B. splitting this function in two makes the code a few ms faster
    def findStartAndCountBlocks(grid):
        counter = 0
        start = None
        for r in range(m):
            for c in range(n):
                if grid[r][c] == -1:
                    counter += 1
                if grid[r][c] == 1: # cause of being slow
                    start = (r,c)
        return start,counter
    
    # creating useful variables
    start, nbBlocks = findStartAndCountBlocks(grid)
    H = set()
    H.add(start)
    
    # readibility function
    # if new pos is not in path history then recur
    def tmpFunc(grid, new, H, R):
        if new not in H:
            T = H.copy()
            T.add(new)
            recur(grid, new, T, R)
    
    def recur(grid, start, H, R):
        # an obstacle has been reach - incorrect path
        if grid[start[0]][start[1]] == -1:
            return
            
        # goal has been reach
        if grid[start[0]][start[1]] == 2:
            if len(H) == (m*n) - nbBlocks:  # checking 'c'
                R[0] += 1

        # up
        if start[1] >= 1:
            new = (start[0], start[1] - 1)
            tmpFunc(grid, new, H, R)

        # down
        if start[1] < n-1:
            new = (start[0], start[1] + 1)
            tmpFunc(grid, new, H, R)

        # left
        if start[0] >= 1:
            new = (start[0] - 1, start[1])
            tmpFunc(grid, new, H, R)

        # right
        if start[0] < m-1:
            new = (start[0] + 1, start[1])
            tmpFunc(grid, new, H, R)

        return R
    
    return recur(grid, start, H, [0])[0]



# 1st and uncleaned version 
"""
Runtime: 86 ms, faster than 63.99% of Python3 online submissions for Unique Paths III.
Memory Usage: 14 MB, less than 17.26% of Python3 online submissions for Unique Paths III.
"""
def uniquePathsIII_2(grid):
    m = len(grid)
    n = len(grid[0])
    
    def findStart(grid):
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return (r,c)
        return None

    def countBlocks(grid):
        counter = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == -1:
                    counter += 1
        return counter
    
    
    start = findStart(grid)
    nbBlocks = countBlocks(grid)
    H = set()
    H.add(start)
    
    def recur(grid, start, H, R):
        if grid[start[0]][start[1]] == -1:
            return
            
        if grid[start[0]][start[1]] == 2:
            if len(H) == (m*n) - nbBlocks:
                R[0] += 1

        # up
        if start[1] >= 1:
            new = (start[0], start[1] - 1)
            if new not in H:
                T = H.copy()
                T.add(new)
                recur(grid, new, T, R)

        # down
        if start[1] < n-1:
            new = (start[0], start[1] + 1)
            if new not in H:
                T = H.copy()
                T.add(new)
                recur(grid, new, T, R)

        # left
        if start[0] >= 1:
            new = (start[0] - 1, start[1])
            if new not in H:
                T = H.copy()
                T.add(new)
                recur(grid, new, T, R)

        # right
        if start[0] < m-1:
            new = (start[0] + 1, start[1])
            if new not in H:
                T = H.copy()
                T.add(new)
                recur(grid, new, T, R)

        return R
    
    return recur(grid, start, H, [0])[0]