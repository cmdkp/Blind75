class Solution:
    def reverseBits(self, n: int) -> int:
            
        rtn = 0
        mask = 1
        for i in range(32):
            if (n & mask):
                t = 1 << 31-i
                rtn = rtn + t
            mask = mask << 1

        return rtn



# More bit operation way that I did before: 
# But is same runtime anyways

class Solution:
    def reverseBits(self, n: int) -> int:
       
       rtn = 0

       for i in range(32):
           bit = (n >> i) & 1
           rtn = rtn | (bit << (31 - i))

       return rtn
