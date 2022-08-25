# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:21:00 2022

@author: david

LeetCode - Easy 1108. Defanging an IP Address
"""

def defangIPaddr(address):
    return "".join([c if c!="." else "[.]" for c in address])

