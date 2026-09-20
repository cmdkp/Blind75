## Step 1: Understand the problem

- Given n integer array nums, we want to return true if any value appears more than once in the array. Otherwise return false.

## Step 2: Working through the problem

First thought:
- Can keep a dict with key value pairs of number and false.
- If repeated num appears, can set value to true and return true

Second thought:
- USE SETS


## Step 3: Plain English Algo

set = ()

for num in nums:
    if num in set:
        return true
    else:
        s.add(num)
        
return false
        
