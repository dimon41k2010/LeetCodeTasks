class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
#         n = len(grid)
#         for r in range(n):
#             for c in range(n):
#                 if r == c or r == n - 1 - c:
#                     if grid[r][c] == 0:
#                         return False
#                 elif grid[r][c] != 0:
#                     return False 
#         return True
    
    
#Time: O(N * M) => O(N)
#Space: O(1)

        index_r = 0
        index_l = len(grid[0])-1

        for r in grid:
            for i in range(len(r)):
                if i == index_r or i == index_l:
                    if r[i] == 0:
                        return (False)
                elif r[i] != 0:
                    return (False)
            index_r += 1
            index_l -= 1
        return (True)