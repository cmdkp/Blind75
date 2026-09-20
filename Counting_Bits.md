## Step 1: Understand the problem

Problem: 
- Given an integer (n), count the number of 1s in the binary representation of every number in the range [0, n]

- Return an array output where output[i] is the number of 1s in the binary representation of i

Constraints:
- n can be 0

## Step 2: Working through the problem

First thought:
- Builds off of last problem (Number of 1 Bits) where number of 1 bits were counted for a single integer so only need do use a for loop to repeat the process for all ints up to n. 
- Will try to use different method than for loop one from last problem

## Step 3: Plain English Algo

lst = []
for i in range(n + 1):
    lst.append(bin(i).count('1'))

return lst
