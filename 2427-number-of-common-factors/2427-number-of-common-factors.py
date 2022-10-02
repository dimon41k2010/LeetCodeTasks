class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        for num in range(1, min(a,b) + 1):
            if a % num == 0 and b % num == 0:
                res += 1
        return (res)

#Time: O(N)
#Space: O(1)