# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 22:55:13 2022

@author: david

LeetCode - Easy 1. Two Sum

Done 1 year, 10 months ago
Too complicated - see solution in discussions
"""

class Solution:
    def endOfValidNums(self, nums, target):
        """This function is used in order to reduce nums' length so it will optimize search algorithims
            if the solution is found, it will return the two values in a List
            otherwise in will return the cutted List
        """
        
        a = 0
        b = len(nums)
        halfpow = (a+b)//2
        
        while (b-a)>1:
            tmp = nums[halfpow]
            tmp_0 = nums[0]
            if (tmp==target & (0 in nums)):
                return sorted([0,tmp])
            
            if (tmp+tmp_0==target):
                return sorted([tmp_0,tmp])
            
            if (tmp+nums[0]>target):
                b = halfpow
                halfpow = (a+b)//2
                
            else:
                a = halfpow
                halfpow = (a+b)//2
                
        return nums[0:halfpow+1]
    
    def searchPair(self, nums, target, a):
        """Given an integer a from nums search if there's a valid pair that will reach the target
            nums must start from a to the last
        """
        
        length = len(nums)
        first = 0
        b = len(nums)
        halfpow = (first+b)//2
        
        while (b-first)>1:
            tmp = nums[halfpow]
            if (tmp+a==target):
                return [True,tmp]
            
            if (tmp+a>target):
                b = halfpow
                halfpow = (first+b)//2
                
            else:
                first = halfpow
                halfpow = (first+b)//2
                
        if (halfpow<=length & halfpow>=0 and (a+nums[halfpow]==target)):
            return [True,nums[halfpow]]
        
        return [False,a]
    
    
    
    def searchTwoIntegers(self, nums, target): 
        if len(nums)==2:
            return nums
        
        for i in range(0,len(nums)):
            res = self.searchPair(nums[i+1:],target,nums[i])
            if (res[0]):
                return [nums[i],res[1]]
        
        return [nums[0],nums[0]]
    
        
            
    
    def twoSum(self, nums, target):
        tmpDict = dict()
        
        for i in range(0,len(nums)):
            if nums[i] in tmpDict:
                tmpDict[nums[i]].append(i)
            else:
                tmpDict[nums[i]] = [i]
            
        myDict = {k: tmpDict[k] for k in sorted(tmpDict)}
        
        sortedNums = sorted(nums)
        
        new_nums = self.endOfValidNums(sortedNums,target)
        res = self.searchTwoIntegers(new_nums,target)
        
        if (len(myDict[res[0]])==1):
            return sorted([myDict[res[0]][0],myDict[res[1]][0]])
        return sorted([myDict[res[0]][0],myDict[res[1]][1]])
        