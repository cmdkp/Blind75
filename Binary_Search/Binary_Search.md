## Step 1: Understand the problem

Problem: 
- Given an array of distinct ints called nums, that is already sorted in ascending order and an integer target. 

- implement a function to search nums for target and return either its index in nums if it exists or -1 otherwise

Constraints:
- Solution must run in O(logn) time
- all integers in nums are unique
- len(nums) >= 1

## Step 2: Working through the problem

First thought:
- Binary search: check number in middle of array and check if target is bigger or smaller than it, and recurse into sub array equivalently
- Make sure to include base case of len of array = 1


## Step 3: Plain English Algo

search (nums, target):

Base case:
- zif len(nums) == 1:
    if nums[0] == target:
        return True
    return False
    
ind = len(nums) // 2

if nums[ind] < target:
    return ind + search (nums[ind:], target)
else:
    return search (nums[:ind + 1], target)
