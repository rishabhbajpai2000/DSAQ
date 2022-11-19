class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # making a dp array 
        dp = []
        cap = 2
        for i in range(len(prices)):
            first_local = []
            for j in range(2):
                local = []
                for k in range(3):
                    local.append(-1)
                first_local.append(local)
            dp.append(first_local)
                
        def helper(ind, buy,cap):
            if ind== len(prices) or cap == 0:
                return 0;
            
            if dp[ind][buy][cap] != -1: return dp[ind][buy][cap]
            
            if buy == 1:
                dp[ind][buy][cap] = max(-prices[ind] + helper(ind+1, 0, cap), 0 + helper(ind + 1, 1, cap))
                return dp[ind][buy][cap]
            dp[ind][buy][cap] =  max(prices[ind] + helper(ind+1, 1, cap-1), 0 + helper(ind+1, 0, cap))
            return dp[ind][buy][cap]
        
        
        return helper(0, 1, cap)