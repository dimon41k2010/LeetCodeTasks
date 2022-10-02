class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        def sum_square(r_, c_, grid):
            res = 0
            for r in range(r_, r_+3):
                for c in range(c_, c_+3):
                    res += grid[r][c]
            return res - grid[r_+1][c_] - grid[r_+1][c_+2]

        res = 0
        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                print(r,c, sum_square(r,c,grid))
                res = max(sum_square(r,c,grid), res)
        
        return (res)

#Time: O(N * M)
#Space: O(1)