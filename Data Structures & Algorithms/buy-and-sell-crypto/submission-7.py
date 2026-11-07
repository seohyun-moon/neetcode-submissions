class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0

        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                best = max(best, profit)
        
        return best