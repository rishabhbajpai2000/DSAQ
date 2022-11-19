class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find global minima till now
        minima = []
        minima.append(prices[0])
        
        for i in range(1,len(prices)):
            if prices[i]<minima[i-1]:
                minima.append(prices[i])
            else:
                minima.append(minima[i-1])
        
        global_profit = 0
        for i in range(len(prices)):
            profit = prices[i]-minima[i]
            global_profit = max(profit, global_profit)
        
        return global_profit
        
        