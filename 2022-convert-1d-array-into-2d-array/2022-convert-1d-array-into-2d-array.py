class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original) != m * n:
            return []
        
        index = 0
        
        res = []
        for r in range(m):
            new_row = []
            for c in range(n):
                new_row.append(original[index])
                index += 1
            res.append(new_row) 
        return res
    
        