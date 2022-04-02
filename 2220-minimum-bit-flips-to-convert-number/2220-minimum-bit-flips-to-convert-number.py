class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        remaining = start^goal
        res = 0
        while remaining:
            res += remaining % 2
            remaining //= 2

        return res

# Time: O(log N) // N = max(start, goal)
# Space: O(1)