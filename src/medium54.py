# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:57:44 2022

@author: David

LeetCode - Medium 54. Spiral Matrix
"""

# my solution
import numpy as np
def recurSpiral(matrix, L):
    if matrix.size != 0:
        L += list(matrix[0])
        matrix = np.delete(matrix, 0, 0)
        matrix = np.rot90(matrix)
        recurSpiral(matrix,L)
    else:
        return

def spiralOrder(matrix):
    L = []
    recurSpiral(np.array(matrix),L)
    return L

# first thought
class Solution:
    def spiralOrder(matrix):
        maxRow = len(matrix)
        maxCol = len(matrix[0])
        total = maxRow*maxCol
        k = maxCol
        L = matrix[0]
        
        maxRow -= 1; maxCol -= 1; miniCol = 0; miniRow = 0
        row = 1; col = maxCol
        
        updateRow = False; updateCol = False
        
        while k < total:
            L.append(matrix[row][col])
            print(f"k = {k}")
            if updateRow or col == maxCol:
                print("A")
                if not updateRow:
                    maxCol -= 1
                    updateRow = True
                    updateCol = False
                row += 1
                continue
            
            if updateCol or row == maxRow:
                print("B")
                if not updateCol:
                    maxRow -= 1
                    updateCol = True
                    updateRow = False
                col -= 1
                continue
                
                
            if updateRow or col == miniCol:  
                print("C")
                if not updateRow:
                    miniCol += 1
                    updateRow = True
                    updateCol = False
                row += 1
                continue
            
            if updateCol or row == miniRow:
                print("D")
                if not updateCol:
                    miniRow += 1
                    updateCol = True
                    updateRow = False
                col += 1
                continue
            k += 1
        return L
    
# one-liner from discussion
# return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])