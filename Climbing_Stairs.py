class Solution:
    def climbStairs(self, n: int) -> int:

        s = 0 # num of 1s
        t = 0 # num of 2s


        count = 1 # base case of 1s
        if n % 2 == 0:
            t = n / 2
        else:
            t = n // 2
            s = 1
        
        while s != n:
            count += (math.factorial(int(s + t)))/(math.factorial(int(s)) * math.factorial(int(t)))

            t -= 1
            s += 2

        
        return int(count)
        
# Dynamic Programming Method:
class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [-1] * n

        def dfs(i):
            if i == n:
                return 1
            
            if i == n-1:
                return 1
            
            if memo[i] != -1:
                return memo[i]
        
            memo[i] = dfs(i+1) + dfs(i+2)

            return memo[i]

        return dfs(0)
