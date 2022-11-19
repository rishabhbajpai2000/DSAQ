class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find global minima till now
        mini = prices[0]
        maxprofit = 0
        for i in range(1,len(prices)):
            cost = prices[i] - mini
            maxprofit = max(maxprofit, cost)
            mini = min(mini, prices[i])

        return maxprofit
        
        