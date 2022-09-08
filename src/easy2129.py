# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:33:55 2022

@author: david

LeetCode - Easy 2129. Capitalize the Title
"""


# my soltuion 
def capitalizeTitle(title):
    # lowering all title string
    s = title.lower()
    
    R = []
    # transforming each word accordingly
    for word in s.split(" "):
        if len(word)>2: R.append(word.capitalize())
        else: R.append(word)
    return " ".join(R)
        

# from accepted - 
def capitalizeTitle2(title):
    # splitting and lowering
    title = title.lower().split()
    
    # modifying accordingly directly in title
    for i in range(len(title)):
        if len(title[i]) > 2:
            title[i] = title[i].title()
    return ' '.join(title)