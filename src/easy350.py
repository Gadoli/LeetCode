# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:59:18 2021

LeetCode - Intersection of Two Arrays II (easy 350)

@author: david
"""

import copy

class Solution:
    def intersect(self, nums1, nums2):
        nums2_copy = copy.copy(nums2)
        R = []
        for i in nums1:
            if i in nums2_copy:
              R.append(i)
              nums2_copy.remove(i)
        return R
             
    
A = Solution()
    
print(A.intersect([1,2,2,1], [2,2]))