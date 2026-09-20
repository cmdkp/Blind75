class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        bit = int(1)
        for i in range(32):
            print(bit)
            if (n & bit):
                count += 1
            bit = bit << 1

        return count

