# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:57:50 2022

@author: david

LeetCode - Medium 122. Bset Time to Buy and Sell Stock II
"""

def maxProfit(prices):
        left = 0
        right = 1
        maxprofit = 0

        while right < len(prices):
            currentprofit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                maxprofit += currentprofit
            left = right
            right += 1
        return maxprofit