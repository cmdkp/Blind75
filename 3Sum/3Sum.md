## Step 1: Understand the problem

Problem:

- Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j, and k are all distinct. 

- The output should NOT contain any duplicate triplets.
- You may return the output and the triplets in any order

Constraints:
- nums.length >= 3
- numbers can be pos, neg, or zero

## Step 2: Working through the problem

First thought:
- Sort the numbers, two pointer approach?

Second thought: 
- Two sum for every number in the array

- This worked but is O(n^2). There has to be a better way


## Step 3: Plain English Algo
rtn = []
for num in nums:

    goal = 0 - num

    d = {}

    for n in nums:
        if (goal - n) in d:
            s = set((goal-n, n, goal))
            if s not in rtn:
                rtn.append(s)
        d[n] = 0

return rtn
