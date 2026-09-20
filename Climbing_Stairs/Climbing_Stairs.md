## Step 1: Understand the problem

Problem: 
- Given an int (n) representing the number of steps to reach the top of a staircase, and knowing we can slimb with either 1 or 2 steps at a time, return the number of distinct ways to climb to the top of the staircase.

Constraints:
- 1 <= n <= 45


## Step 2: Working through the problem

First thought:
- permutations and factorials

ex. for n=4, it is 1 (base case of all 1s) + 3! (values 1, 1, 2) / 2! (because 1 is repeated twice)

## Step 3: Plain English Algo

while the number of 1s we have is not equal to n:
    do the factorial calculation
    update the values for 1 and 2 with +1 + 1 and -2
