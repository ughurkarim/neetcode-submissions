class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0

        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            leftP = prices[l]
            rightP = prices[r]

            profit = rightP-leftP

            maxProfit = max(maxProfit, profit)

            if leftP > rightP:
                l += 1
            elif rightP >= leftP:
                r += 1
        
        return maxProfit
        
        
        