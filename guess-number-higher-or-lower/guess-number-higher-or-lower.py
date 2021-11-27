# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2
            pick = guess(mid)
            if pick == 0:
                return mid
            elif pick == 1:
                left = mid + 1
            elif pick == -1:
                right = mid - 1
        return -1
    
# Time: O(log N) Binary search
# Space: O(1)