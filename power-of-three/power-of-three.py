import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
#         def is_power(n):
#             if n == 0:
#                 return False
            
#             if n == 1:
#                 return True
#             if n % 3 != 0:
#                 return False
#             return is_power(n/3)

#         return(is_power(n))

# Time: O(log(3) N)
# Space: O(log(3) N)


# Binary search
        if n == 0:
            return(False)
        if n == 1:
            return (True)

        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            
            num = 1
            count = 0
            while count < mid and num < n:
                    num *= 3
            if n == num:
                return(True)
                
            elif num > n:
                right = mid - 1
            elif num < n:
                left = mid + 1
        return(False)

# Time: O(log N) * O(N)
# Space: O(1)