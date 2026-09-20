## Step 1: Understand the problem

Problem: 
- Given an array of ints (nums) and a integer k, return the k most frequent elements within the array

Constraints:
- output can be returned in any order

## Step 2: Working through the problem

First thought:
- count frequencies and store them in a dict. Then, sort by the values and return the top k related keys

## Step 3: Plain English Algo

d = {}

for num in nums:
    if num not in d:
        d[num] = 1
    
    else:
        d[num] = d[num] + 1
    
vals = d.values()
vals = d.sorted(vals, reverse=True)

rtn = []
for i in range k:
    rtn.append(d.getKey(vals[i]))
    
return rtn
