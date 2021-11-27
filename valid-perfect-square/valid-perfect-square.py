class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid -1
            elif mid * mid < num:
                left = mid + 1
        return False

# Time: O(log N) Binary search
# Space: O(1)