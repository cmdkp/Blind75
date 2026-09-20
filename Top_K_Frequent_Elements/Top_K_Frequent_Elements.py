class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            
            else:
                d[num] = d[num] + 1
        
        dtups = [(x,y) for (x,y) in d.items()]
        dtups = sorted(dtups, key=lambda x: x[1], reverse=True)

        rtn = []

        for i in range(k):
            rtn.append(dtups[i][0])

        return rtn
