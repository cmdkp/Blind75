# First thought:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        n = min(nums)

        if n < 0:
            nums = [n * (-1) + i for i in nums]
        
        m = max(nums)

        rtnlist = [0] * (m+1)

        for n in nums:
            rtnlist[n] = 1

        ctr = 0
        ls = []

        print(rtnlist)
        for i in rtnlist:
            if i == 0 and ctr > 0:
                ls.append(ctr)
                ctr = 0
            elif i == 1:
                ctr += 1
        
        if not ls and ctr > 0 or ctr > max(ls):
            return ctr
        
        return max(ls)
        
# second method with dict was also too slow:
if not nums:
            return 0

        d = {}
        for i in nums:
            d[i] = 1

        l = min(nums)
        m = max(nums)

        ctr = 0
        ls = []
        for i in range(l, m+1):
            if i in d:
                ctr += 1
            elif ctr > 0:
                ls.append(ctr)
                ctr = 0
        
        if not ls and ctr > 0 or ctr > max(ls):
            return ctr
        
        return max(ls)
        
        
        
# Solution which worked:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        ns = sorted(nums)
        # has to have at least 1 element

        s = []
        s.append(ns[0])

        for n in ns:
            if s[-1] != n:
                s.append(n)

        ctr = 0
        ls = []
        print(s)
        for i in range(1, len(s)):
            if s[i] == s[i-1] + 1:
                ctr += 1
            elif ctr > 0:
                ls.append(ctr)
                ctr = 0
        
        if not ls:
            if ctr > 0:
                return ctr + 1
            return 1
        
        if ctr + 1 > max(ls):
            return ctr + 1

        
        return max(ls) + 1

