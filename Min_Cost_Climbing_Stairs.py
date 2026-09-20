class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        rtn = 0

        pos = 0
        if cost[1] <= cost[0]:
            pos = 1

        while pos < len(cost):
            
            rtn += cost[pos]

            if pos + 1 == len(cost) or pos + 2 == len(cost):
                break
            
            if cost[pos + 1] < cost[pos + 2] and not pos + 4 == len(cost):
                pos += 1
            else:
                pos += 2

        rtn1 = rtn

        rtn = 0

        pos = len(cost) - 1
        if cost[len(cost) - 2] <= cost[len(cost) - 1]:
            pos = len(cost) - 2

        while pos > -1:
            
            rtn += cost[pos]

            if pos - 1 == -1 or pos - 2 == -1:
                break
            
            if cost[pos - 1] < cost[pos - 2] and not pos - 4 == -1:
                pos -= 1
            else:
                pos -= 2


        return min(rtn, rtn1)


# Dynamic Programming Method:

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [-1] * len(cost)

        def dfs(i):
            if i > len(cost)-1:
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]

        return min(dfs(0), dfs(1))
            
