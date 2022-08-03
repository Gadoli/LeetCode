# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 20:32:04 2022

@author: david

LeetCode - Medium 729. My Calendar I
"""

class MyCalendar:

    def __init__(self):
        self.mC = []
        
    
    def book(self, start: int, end: int) -> bool:
        # case when MyCalendar is empty
        if not self.mC:
            self.mC = [[start,end]]
            return True 
        
        # case appending in the end
        if self.mC[-1][1]<=start:
            self.mC.append([start,end])
            return True 
            
        # case appending in the start
        elif end <= self.mC[0][0]:
            self.mC.insert(0,[start,end])
            return True 
        
        # other cases
        for i in range(len(self.mC)-1):
            # case when inside a booked time
            if self.mC[i][0] <= start and end <= self.mC[i][1]: return False
            if self.mC[i][1] <= start and end <= self.mC[i+1][0]:
                self.mC.insert(i+1,[start,end])
                return True 
        
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)