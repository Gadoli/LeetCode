# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:47:10 2021

LeetCode - Buddy Strings (easy 859)

@author: david
"""

def buddyStrings(s, goal):
    if len(s)!=len(goal):
        return False
    diff = 0
    L_s = []
    L_goal = []
    for i in range(len(s)):
        if s[i]!=goal[i]:
            diff+=1
            L_s.append(s[i])
            L_goal.append(goal[i])
    if diff>2 or diff==1:
        return False
    if diff==2:
        L_s.sort()
        L_goal.sort()
        return L_s==L_goal
    for i in s:
        if s.count(i)>1:
            return True
    return False
