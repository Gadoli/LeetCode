# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:17:43 2022

@author: david

LeetCode - 1603. Design Parking System
"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        
    def addCar(self, carType: int) -> bool:
        if carType==1 and self.big: 
            self.big -= 1
            return True
    
        if carType==2 and self.medium:
            self.medium -= 1
            return True 
        
        if carType==3 and self.small:
            self.small -= 1
            return True    
        
        return False
                


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)