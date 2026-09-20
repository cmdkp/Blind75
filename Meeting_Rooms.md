## Step 1: Understand the problem

Problem: 
- Given an array of meeting time interval objects consisting of start and end times, determine if a person could add all meetings to their schedule without any conflicts.
- The intervals may be provided in any order

- Note: end time of interval a = start time of interval b does not mean conflict

Constraints:
- len(intervals) can be 0

## Step 2: Working through the problem

First thought: 
- Sort the intervals by finishing time. Check if any start times happen before finishing time of prev interval. 

## Step 3: Plain English Algo

if len(intervals) == 1 or len(intervals) == 0:
    return True

intervals.sort(key=lambda interval: interval[1])

for i in range(len(intervals) - 1, 1):
    if intervals[i][0] < intervals[i-1][1]:
        return False
        
return True

    


