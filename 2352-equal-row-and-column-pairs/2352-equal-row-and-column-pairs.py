class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        def to_string(arr): # [3,1,2,2] => "3,1,2,2"
            return ",".join([ str(val) for val in arr])

        count_col = {}
        for c in range(len(grid[0])):
            arr = []
            for r in range(len(grid)):
                arr.append(grid[r][c])
            key = to_string(arr)
            if key not in count_col.keys():
                count_col[key] = 1
            else:
                count_col[key] += 1

        count_row = {}
        for row in grid:
            key = to_string(row)
            if key not in count_row.keys():
                count_row[key] = 1
            else:
                count_row[key] += 1

        res = 0
        for key in count_row.keys():
            if key in count_col.keys():
               res += count_row[key] * count_col[key]
        return (res)

    
#Time: O(N * M) // N=grid[0], M=len(grid)
#Space: O(N * M) // N=grid[0], M=len(grid)