class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minima = prices[0]
        maxprofit = 0
        
        for price in prices:
            curprof = price - minima
            maxprofit = max(maxprofit, curprof)
            minima = min(minima, price)
        return maxprofit
        