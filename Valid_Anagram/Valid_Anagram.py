# Solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        nums = {}

        for i in range(len(s)):
            if (s[i] in nums):
                nums[s[i]] += 1
            else:
                nums[s[i]] = 1

            if (t[i] in nums):
                nums[t[i]] -= 1
            else:
                nums[t[i]] = -1
        
        
        for x in nums.values():
            if x != 0:
                return False

        return True

            


                
#Solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sd, td = {}, {}
        for i in range(len(s)):
            sd[s[i]] = sd.get(s[i], 0) + 1
            td[t[i]] = td.get(t[i], 0) + 1

        return sd == td
