class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            sum_mid = (mid * (mid + 1)) / 2
            if sum_mid <= n:
                left = mid + 1
            elif sum_mid > n:
                right = mid - 1

        return (right)

# Time: O(log N) Binary search
# Space: O(1)