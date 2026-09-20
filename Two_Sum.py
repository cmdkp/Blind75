class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}
        for i, e in enumerate(nums):
            c = target - e
            if c in map:
                return [map[c], i]
            map[e] = i
        


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i in range(len(nums)):
            if (target-nums[i] in d):
                return [d[target-nums[i]], i]
            else:
                d[nums[i]] = i

        return [0, len(nums) - 1]
        
