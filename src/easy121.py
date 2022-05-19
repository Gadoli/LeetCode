# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 20:04:00 2022

@author: david

LeetCode - Easy 121. Bset Time to Buy and Sell Stock
"""

def maxProfit(prices):
    left = 0
    right = 1
    maxprofit = 0
    
    while right < len(prices):
        currentprofit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            maxprofit = max(maxprofit,currentprofit)
        else:
            left = right
        right += 1
    return maxprofit
        