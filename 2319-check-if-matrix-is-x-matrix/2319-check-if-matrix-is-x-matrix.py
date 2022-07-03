class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if r == c or r == n - 1 - c:
                    if grid[r][c] == 0:
                        return False
                elif grid[r][c] != 0:
                    return False 
        return True
    
    
#Time: O(N * M) => O(N)
#Space: O(1)