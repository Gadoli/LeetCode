# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:23:13 2022

@author: David

LeetCode - Medium 621. Task Scheduler
"""
import collections

# from disuccsion - commented and understood
def leastInterval(tasks, n):
    # counting frequency of tasks : 3A 3B 1C -> 3 3 2
    task_counts = collections.Counter(tasks).values()
    
    # getting the max frequency : 3A 3B 1C -> 3
    M = max(task_counts)
    
    # counting the number of task having max frequency : 3A 3B 1C -> 2
    Mct = list(task_counts).count(M)
    
    """
    if enough different tasks to have no idles : res is len(tasks)
    else too much tasks, some idles are needed, 
    res =
        number of 'chunk' used to do the tasks (includes idles) (not counting excess)
        * length of a chunk (max length before using same letter) (include idles)
        + remaning tasks to do (no idles since their the last ones)
    e.g. : 5A 1B 1C , n = 2 -- M = 5, Mct = 1
    (ABC)(A__)(A__)(A__) : (M-1)
    A _ _ : (n + 1)
    A : Mct
    ABCA__A__A__A
    """
    return max(len(tasks), (M - 1) * (n + 1) + Mct)



# Time Limit Exceeded on LeetCode
# works off-line though
# greedy solution not efficient
from collections import Counter

def usable(R, value, n):
    # chcking last time value has been used
    if value not in R: return True
    return (R[::-1].index(value))>=n

def specialSort(L):
    # sorting L according to structure used
    return [[k,v] for k,v in Counter(dict(L)).most_common()]

def leastInterval2(tasks, n):
    # getting frequency
    L = [[k,v] for k,v in Counter(tasks).most_common()]
    # index, memory, cooldown
    i = 0
    R = []
    k = n+1

    # going through most frequent task
    while L:
        # end has been reached going back to most frequent
        if i >= len(L): i = 0
        
        # machine has cooldowned
        if k == 0:
            L = specialSort(L)
            i = 0
            k = n+1
        k -= 1
        if usable(R,L[i][0],n):
            L[i][1] -= 1
            R.append(L[i][0])
        else:
            R.append("idle")
            continue

        if L[i][1] == 0:
            del L[i]
            continue

        i += 1
    return len(R)