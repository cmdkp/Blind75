## Step 1: Understand the problem

Problem: 
- Given an array of integer nums, return the length of the longest consecutive sequence of elements that can be formed. 

- Alg must run in O(n) time

Constraints:
- 0 <= nums.length <= 100,000
- numbers in nums can be positive, negative, and zero

## Step 2: Working through the problem

First thought:
- Use a long array and store consecutive orders based off indexes

- That did not work due to memory it takes

Second thought/original thought:
- Sort the elements first and then use a counter

## Step 3: Plain English Algo

if not nums:
    return 0

n = min(nums)

if n < 0:
    nums = [n * (-1) + i for i in nums]

m = max(nums)

rtnlist = [0] * (m+1)

for n in nums:
    rtnlist[n] = 1

ctr = 0
ls = []

print(rtnlist)
for i in rtnlist:
    if i == 0 and ctr > 0:
        ls.append(ctr)
        ctr = 0
    elif i == 1:
        ctr += 1

if not ls and ctr > 0 or ctr > max(ls):
    return ctr

return max(ls)
