## Step 1: Understand the problem

Problem: 
- Given an array of strings (strs), group all anagrams together into sublists.
- Output can be returned in any order but structure is list of lists

- Anagrams are strings which contain same letters but have different orders

Constraints:
- list has at least 1 element in it
- length of strings can be 0
- each word is in lowercase


## Step 2: Working through the problem

First thought:
- Create a dict with key=set and val=strings from the list. Can go through the strings, split them by letters and add them to a set, and if that set exists in the dict, then add the str to the related value list. Otherwise, create a new entry in the dict. At the end, return the list of values of the dict

## Step 3: Plain English Algo

d = {}

for st in strs:
    s = set()
    s.add(st.split())
    # [s.add(s) for s in str.split()]
        
    if s in d:
        d[s].append(st)
    else:
        d[s] = [str]

return d.values()
