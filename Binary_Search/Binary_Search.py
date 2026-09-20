class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # two pointer approach
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            ind = l + ((r - l) // 2)
            if nums[ind] == target:
                return ind
            elif nums[ind] > target:
                r = ind - 1
            elif nums[ind] < target:
                l = ind + 1

        return -1
        
        
        
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # recursion approach
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1

        
        mid = (len(nums) - 1) // 2
        if nums[mid] > target:
            # target in first half
            return self.search(nums[:mid + 1], target)
        elif nums[mid] < target:
            rtn = self.search(nums[mid + 1:], target)
            if rtn == -1:
                return -1
            return mid + rtn + 1
        else:
            return mid
