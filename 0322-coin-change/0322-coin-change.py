class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def helper(index, target):
            if index == 0:
                if target%coins[0] == 0: return target//coins[0]
                else: return 10_0009
            
            if dp[index][target] != -1: return dp[index][target]
            
            
            nottaken = 0 + helper(index-1, target)
            taken = 10_0009
            if coins[index]<= target:
                taken = 1 + helper(index, target - coins[index])
            dp[index][target] = min(taken, nottaken)
            return dp[index][target]

        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        ans = helper(len(coins) -1, amount)
        if ans <= 10_000:
            return ans
        return -1