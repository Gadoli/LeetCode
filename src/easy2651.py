# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:28:53 2023

@author: david

LeetCode - Easy 2651. Calculate Delayed Arrival Time
"""

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime)%24
