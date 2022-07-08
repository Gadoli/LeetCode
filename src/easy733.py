# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 8:08:18 2022

@author: david

LeetCode - Easy 733. Flood Fill
"""

class Solution:
    def dfs(self, image, sr, sc, color, startColor):
        if image[sr][sc] == color: return None
        if image[sr][sc] == startColor: image[sr][sc] = color
        else: return None
        
        if sr > 0: self.dfs(image,sr-1,sc,color,startColor)
        if sr < len(image) - 1: self.dfs(image,sr+1,sc,color,startColor)
        if sc > 0: self.dfs(image,sr,sc-1,color,startColor)
        if sc < len(image[0]) - 1: self.dfs(image,sr,sc+1,color,startColor)
                    
        return image
    
    
    def floodFill(self, image, sr, sc, color):
        startColor = image[sr][sc]
        self.dfs(image,sr,sc,color,startColor)
        return image