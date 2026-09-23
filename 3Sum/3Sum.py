class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        rtn = []
        for i, num in enumerate(nums):

            goal = 0 - num

            d = {}

            for j, n in enumerate(nums):
                if i == j:
                    continue
                if (goal - n) in d:
                    s = sorted([goal-n, n, num])
                    if s not in rtn:
                        rtn.append(s)
                d[n] = 0
        
        return rtn

            
