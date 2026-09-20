## Step 1: Understand the problem

Problem: 
- Given an array of ints (cost) where cost[i] is the cost of taking a step from the ith floor of a staircase
- Can step to either i=1th or i+2th floor after paying cost of ith floor
- Can choose to start at floor/index 0 or 1

- Return min cost of getting to top (1 index after last index in cost list) of staircase

Constraints:
- Guaranteed that cost list is at least len=2 (index 0 and index 1)

## Step 2: Working through the problem

First thought:
- Go upwards by always picking the lowest cost out of index i+1 and i+2 (and start by picking lowest out of index 0 and index 1

- Did not work cause of edge case: [1, 2, 3] where code returns 3 but correct ans is 2

Next attempt:
- Same logic, but go downwards from the top of the staircase so that the 2 in the edgecase is considered

- Also did not work due to similar edge case from reverse: [0, 2, 2, 1]

Next attempt:
- Do front logic first, store that value, and then do backwards logic, and return min out of both

- Also did not work due to edgecases again. The second last value kept breaking logic
- Other test cases which have failed so far: [0, 2, 3, 2], [1, 0, 0, 1]


- Won by adding special check for second last characters and going upwards and downwards
- In total, took 1h 14min (started at 11:50 PM too so ended at 1 AM but completed it without help)

## Step 3: Plain English Algo

def minCostClimbingStairs(self, cost: List[int]) -> int:
    
    rtn = 0

    pos = 0
    if cost[1] <= cost[0]:
        pos = 1

    while pos < len(cost):
        
        rtn += cost[pos]

        if pos + 1 == len(cost) or pos + 2 == len(cost):
            break
        
        if cost[pos + 1] < cost[pos + 2]:
            pos += 1
        else:
            pos += 2

    return rtn

