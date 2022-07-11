# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 22:01:18 2022

@author: david

LeetCode - Easy 746. Min Cost Climbing Stairs
"""

def minCostClimbingStairs(cost):
    n = len(cost)
    
    first = cost[0]
    second = cost[1]
    
    if n<=2: return min(first,second)
    
    for i in range(2,n):
        curr = cost[i] + min(first,second)
        first = second
        second = curr
    return min(first,second)
            
        