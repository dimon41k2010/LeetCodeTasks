class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        for row in matrix:
            if n != len(set(row)):  #Time: O(N)
                return False

        for c in range(n):
            set_ = set()
            for r in range(n):
                set_.add(matrix[r][c])
            if n != len(set_):
                return False
        return True


# Time: O(N^2) //  len(matrix) * set(row)
# Space: O(N) 