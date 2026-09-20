# O(n) but using the division operation:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        y = 1
        x = 1
        zc = 0

        for n in nums:

            if n != 0:
                y *= n
            else:
                zc += 1

            x *= n

        if zc > 1:
            return len(nums) * [0]

        rtn = []

        for n in nums:
            if n == 0:
                rtn.append(y)
            else:
                rtn.append(int(x / n))

        return rtn
    
