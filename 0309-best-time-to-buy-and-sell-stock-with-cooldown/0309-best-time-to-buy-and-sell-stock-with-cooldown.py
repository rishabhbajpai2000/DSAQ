class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def helper(index, buy):
            if index >= len(prices): return 0
            if dp[index][buy] != -1: return dp[index][buy]
            if buy == 1: 
                dp[index][buy] = max(-1* prices[index] + helper(index+1, 0), \
                           0 + helper(index+1, 1))
                return dp[index][buy]
            
            dp[index][buy] = max(prices[index] + helper(index+2, 1), \
                      0 + helper(index + 1, 0) )
            return dp[index][buy]
        
        index = 0
        buy = 1
        dp = [[-1] * 2 for _ in range(len(prices))]
        return helper(index, buy)