## Step 1: Understand the problem

Problem: 
- Given an array (nums) containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums

Constraints:
- len(nums) >= 1

## Step 2: Working through the problem

n = len(nums)

First thought:
- Use a dict with numbers as keys, set everything default to false, and when a number is found key value in dict associated with key to true. Then at end return key with the only false remaining value

- This is O(n) time complexity but it is not O(1) space complexity

Second thought
- Calculate sum of all nums from 0 to n at start, per number found delete it from the sum. At the end the remaining sum is the missing number

- And this is O(1) space too


## Step 3: Plain English Algo

sum = (n(n+1)) / 2

for num in nums:
    sum -= num
    
return sum


