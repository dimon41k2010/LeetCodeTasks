class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 0:
            return (False)

        def is_pow(n):
            if n == 1:
                return True
            if n % 2 != 0:
                return False
            return is_pow(n/4)

        return (is_pow(n))


# Time: O(log(4) N)
# Space: O(log(4) N)