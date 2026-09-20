## Step 1: Understand the problem

Problem: 
- Given array of price of stocks everyday, need to choose a single day to buy the stock and a later date to sell the stock which gives the most profit. Or pick no days if otherwise profit will be negative. Need to return the value of the highest profit. 

Constraints: 
- Sell date of stock needs to be later than buy date
- Can only buy and sell once
- length of array is at least 1 (let this be edge case)


## Step 2: Working through the problem 

- ```[10, 9, 8, 7, 1, 10]```
- ```[10, 1, 5, 6, 7, 5, 10]```

First thought:
- Could do double for loop and store the largest profit amount -> O(n^2) though

Second thought:
- Double pointers at edges of the input array and moving depending on if profit increases or not
- But the problem is no garuntee if moving one pointer will be the right pointer to move
- If profit goes up move my sell, but if profit goes down move my buy and my sell? And store max profit

Third thought (after 30 mins of doing the question):
- Start pointers at the start of the array, keep moving right pointer, only move left pointer if value of right pointer is smaller than it

## Step 3: Plain English Algo

First check if length of array is just one, if so, return 0
Next, maxprofit = prices[1] - prices[0], ptr1 = 0, ptr2 = 1

while (ptr2 != len(prices) - 1) :

    if prices[ptr2] - prices[ptr1] >= max:
        maxprofit = prices[ptr2] - prices[ptr1]
        ptr2 += 1
    else:
        ptr1 += 1
        ptr2 += 1
        
return max(maxprofit, 0)
