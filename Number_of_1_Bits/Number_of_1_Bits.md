## Step 1: Understand the problem

Problem: 
- Given an unsigned int (n) and return the number of 1 bits in its binary representation

Constraints:


## Step 2: Working through the problem

First thought:
- Unsigned int is 32 bits, and bitwise AND (x&y) will return something if 1&1 and 0 if 0&1 so can do a for loop for range 32 and at each iteration, shift the 1 in a checker value by 1 bit to the left and count if something is returned from the bitwise AND. At the end, return the counter

- NOTE: This is called a bitwise mask approach
- NOTE: That worked but rmbr that bitwise shift returns the new value and does NOT modify current value

## Step 3: Plain English Algo

count = 0
bit = 1
for i in range(32):
    if (n & bit):
        count += 1
    bit << 1

return count
