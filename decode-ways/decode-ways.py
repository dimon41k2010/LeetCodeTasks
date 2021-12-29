class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [-1 for _ in s]
        # print(dp)

        def solve_recur(i):

            if i == len(s):
                return 1

            if dp[i] != -1:
                return dp[i]

            if s[i] == "0":
                dp[i] = 0
                return dp[i]

            res = solve_recur(i+1)

            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                res += solve_recur(i+2)
            dp[i] = res

            return dp[i]

        return (solve_recur(0))