class Solution:
    def isValid(self, s: str) -> bool:

        d = {']':'[', ')': '(', '}': '{'}
        arr = []

        for b in s:
            if b in d:
                if len(arr) > 0 and arr[-1] == d[b]:
                    arr.pop()
                else:
                    arr.append(b)
            else:
                arr.append(b)

        return len(arr) == 0
