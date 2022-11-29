class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def helper(index, target):
            if index == 0:
                if target % coins[0] == 0: return 1
                return 0
            if dp[index][target] != -1: return dp[index][target]
            nottake = helper(index-1, target)
            take = 0
            if coins[index] <= target: take = helper(index, target-coins[index])
            
            dp[index][target] = take + nottake
            return dp[index][target]
        
        dp = [[-1]*(amount+1) for _ in range(len(coins))]
        
        return helper(len(coins)-1, amount)