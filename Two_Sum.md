## Step 1: Understand the problem

Problem:
- Given an array of integers (nums) and an integer target, we want to return the indices i and j such that the numbers at indices i and j in nums add up to the target and i != j.

Return answer with the smaller index first

Constraints:
- 2 <= nums.length <= 1000
- Only one valid answer exists


## Step 2: Working through the problem

First thought:
- Make a dict of pairs: {key=(target - nums[index]), value = index}
- Add the value at first index to dict as base case and then start the solution's for loop from the second value.
- At each index, check if target-nums[i] is in the dict and if it is (then we have our two values) , return [index from dict (since it was earlier and was already processed), current index]. Otherwise, add it to the dict
- At the end of the for loop, return [0,len(nums) - 1] but this should never be reached


## Step 3: Plain English Algo

- Create a dict d
- d[0] = target - nums[0]

- At each index, check if target-nums[i] is in the dict (then we have our two values) and if it is, return [index from dict (since it was earlier and was already processed), current index]. Otherwise, add it to the dict
- At the end of the for loop, return [0,len(nums) - 1] but this should never be reached
