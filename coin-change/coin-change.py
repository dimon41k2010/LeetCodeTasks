class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [0]

        for i in range(1,amount+1):
            dp.append(-1)
            for step in coins:
                lookup = i - step
                if lookup < 0 or dp[lookup] == -1:
                    continue
                if dp[i] == -1:
                    dp[i] = dp[lookup] + 1
                else:
                    dp[i] = min(dp[i], dp[lookup] + 1)
        return dp[amount]

# Time: O(N * M) // M=len(coins), N=amount
# Space: O(N) // N=amount
        