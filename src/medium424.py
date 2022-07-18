# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:00:00 2022

@author: david

LeetCode - Medium 424. Longest Repeating Character Replacement

seen and learnt from discussion
"""
   
def characterReplacement(s, k):
    # using a window with left and right
    
    left = 0
    longest_str_len = 0
    c_frequency = {}
    
    for right in range(len(s)):
        
        # updating c_frequency each we see a new cell
        if not s[right] in c_frequency:
            c_frequency[s[right]] = 0
        c_frequency[s[right]] += 1
        
        # counting the range of the cells
        cells_count = right - left + 1
        
        # in the window left~right, checking the replacement cost
        # Replacements cost = cells count between left and right - highest frequency
        if cells_count - max(c_frequency.values()) <= k:
            longest_str_len = max(longest_str_len, cells_count)
        
        # replacements cost exceeds k, update c_frequency, move left to 1
        else:
            c_frequency[s[left]] -= 1
            if not c_frequency[s[left]]:
                c_frequency.pop(s[left])
            left += 1
            
    return longest_str_len