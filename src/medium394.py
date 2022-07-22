# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:46:34 2022

@author: david

LeetCode - Medium 394. Decode String
"""
# from discussion
def decodeString(s):
    stack = []; curNum = 0; curString = ""
    for c in s:
        if c == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ""
            curNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num*curString
        elif c.isdigit():
            curNum = curNum*10 + int(c)
        else:
            curString += c
    return curString


# =============================================================================
# 
# =============================================================================

import functools


def decodeString1(s,tmp,R):
    # WIP
    if not s:
        return R
    
    if s[0].isnumeric():
        tmp.append(int(s[0]))
        return decodeString(s[1:],tmp,R)
        
    if tmp:
        n =functools.reduce(lambda total, d: 10 * total + d, tmp, 0)
        return n * decodeString(s[1:],[],R)
        
    return None

# this code is not working for this instance
# "1[a1[b]c1[d]e]"
class Solution:
    def decodeString2(self, s: str) -> str:
        R = []
        nums = []
        num_tmp = []
        strings = []
        opened = 0
        nested = False
        newNest = False
        for i in s:
            if i.isnumeric():
                num_tmp.append(int(i))
                continue
                
            if num_tmp:
                nums.append(functools.reduce(lambda total, d: 10 * total + d, num_tmp, 0))
                num_tmp = []
            if i=='[':
                opened += 1
                strings.append([])
            elif i.isalpha():
                if not opened:
                    R.append(i)
                elif nested and newNest:
                    strings.append([i])
                    newNest = False
                    postNest = True
                else:
                    strings[-1].append(i)

            else:
                if opened > 1:
                    nested = True
                    newNest = True
                    opened -= 1
                    N = [nums.pop(-1)*"".join(strings[-1])]
                    strings.pop(-1)
                    continue
                
                if not nested and opened==1:
                    R.append(nums.pop(-1)*"".join(strings[-1]))
                    strings.pop(-1)
                    opened -= 1
                
                else:
                    if postNest:
                        N[-1] = nums.pop(-1) * ("".join(strings[-2]) + N[-1] + "".join(strings[-1]))
                        strings.pop(-1)
                        posNest = False
                    else:
                        N[-1] = nums.pop(-1) * ("".join(strings[-1]) + N[-1])
                    strings.pop(-1)
                    opened -= 1
                if nested and not opened:
                    nested = False
                    R.append(N[0])

        return "".join(R)