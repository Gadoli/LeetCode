# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:48:09 2022

@author: david

LeetCode - Easy 1672. Richest Customer Wealth

Runtime: 88 ms, faster than 44.42% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 13.9 MB, less than 73.50% of Python3 online submissions for Richest Customer Wealth.
"""

def maximumWealth(accounts):
    return max([sum(i) for i in accounts])