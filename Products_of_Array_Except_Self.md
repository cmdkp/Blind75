## Step 1: Understand the problem

Problem: 
- Given an integer array nums, return an array output where output[i] is the product of all elements of nums except nums[i]

- Follow-up, can I solve it in O(n) without using the division operation?

Constraints:
- 2 <= nums.length <= 100,000
- -30 <= nums[i] <= 30


## Step 2: Working through the problem

First thought:
- Store a value for the total product of all elements in nums and then create a new array where new[i] is value div nums[i]

- This will be O(n) but will use the division operation


Came back because if there is a 0 in the array, then above approach doesn't work.
Second thought:
- Issue with 0s... can store a second variable only used to store non-zero products. 
- And if ever more than one 0 in the list, then the entire rtn list will be 0s too

- Adding this on top of the first alg worked! So it is O(n) but issue is it still uses the division operation


Third thought:
- 

## Step 3: Plain English Algo
For first thought:

x = 1
for n in nums:
    x *= n
    
rtn = []
for n in nums:
    rnt.append(x / n)

return rtn
