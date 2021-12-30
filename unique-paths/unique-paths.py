class Solution:
    def uniquePaths(self, R: int, C: int) -> int:
        
        dp = [ [ 0 for c in range(C) ] for r in range(R) ]
        dp[-1][-1] = 1

        def solve_recur(r,c):

            if r >= R or c >= C:
                return 0
            # print("ENTER:", r,c, "|",dp[r][c])
            if dp[r][c] != 0:
                # print("exit memo:", r,c, "|",dp[r][c])
                return dp[r][c]

            dp[r][c] = solve_recur(r+1, c) + solve_recur(r, c+1)
            # print("Exit:", r,c, dp[r][c])
            return dp[r][c]

        return (solve_recur(0,0))
    
    
# Time: O(N * M) => O(R * C)
# Space: O(N * M) => O(R * C)

