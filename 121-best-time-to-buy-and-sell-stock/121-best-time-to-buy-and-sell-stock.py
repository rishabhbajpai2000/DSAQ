class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0 
        left = prices[0]
        
        profit = prices[1] - prices[0]
        for right in prices:
            if left > right:
                left = right
            diff = right - left
            profit = max(profit, diff)
        return profit