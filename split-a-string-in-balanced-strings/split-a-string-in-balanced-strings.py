class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_R = 0
        count_L = 0
        res = 0
        for char in s:
            if char == "L":
                count_L += 1
            elif char == "R":
                count_R += 1
            if count_L == count_R:
                res += 1
        return res
    