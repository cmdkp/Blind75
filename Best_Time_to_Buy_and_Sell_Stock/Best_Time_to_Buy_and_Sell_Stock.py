class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1:
            return 0

        maxprofit = prices[1] - prices[0]
        ptr1 = 0

        maxprofit = max(maxprofit, 0)
        for ptr2 in range(1, len(prices)):
            if (prices[ptr2] - prices[ptr1] > maxprofit):
                maxprofit = prices[ptr2] - prices[ptr1]
            
            if (prices[ptr2] < prices[ptr1]):
                ptr1 = ptr2
        
        return max(maxprofit, 0)
