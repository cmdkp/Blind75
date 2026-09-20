class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for st in strs:
            sortedstr = ''.join(sorted(st))
                
            if sortedstr in d:
                d[sortedstr].append(st)
            else:
                d[sortedstr] = [st]

        return list(d.values())
