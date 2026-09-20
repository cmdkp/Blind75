## Step 1: Understand the problem

Problem: 
- Given a 32-bit unsigned integer (n), reverse the bits of the binary representation of n and return the results

- Reverse meaning left to right, not 1 <-> 0

Constraints:


## Step 2: Working through the problem

First thought:
- For loop, bit mask of 1 which moves leftwards along n, and a new rtn value which is added by 1 if bit mask returns something not 0 and left shifted by 32-i per interation


## Step 3: Plain English Algo

rtn = 0
mask = 1
for i in range(32):
    if (n & mask):
        t = 1 << 31-i
        rtn = rtn + t
    mask = mask << 1

return rtn
    
