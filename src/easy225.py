# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 19:02:20 2022

@author: david

LeetCode - Easy 225. Implement Stack using Queues

Runtime: 57 ms, faster than 22.15% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 13.9 MB, less than 98.63% of Python3 online submissions for Implement Stack using Queues.
"""

# usig a list

class MyStack:

    def __init__(self):
        self.L = []

    def push(self, x: int) -> None:
        self.L.append(x)

    def pop(self) -> int:
        if self.L:
            return self.L.pop()
        
    def top(self) -> int:
        if self.L:
            return self.L[-1]

    def empty(self) -> bool:
        return len(self.L)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()