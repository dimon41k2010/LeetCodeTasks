class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        r = m
        c = n

        for point in ops:
            n_r, n_c = point
            r = min(n_r, r)
            c = min(n_c, c)

        return r*c
    
#Time: O(n)
#Space: O(1)