class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
     
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
        def is_perimeter(r, c, grid):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return True
            return grid[r][c] == 0

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    for direction in directions:
                        res += 1 if is_perimeter(r + direction[0], c + direction[1], grid) else 0
        return (res)

#Time: O(N * M)
#Space: O(N * M)