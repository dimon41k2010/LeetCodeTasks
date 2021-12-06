class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def is_power(n):
            if n == 0:
                return False
            
            if n == 1:
                return True
            if n % 3 != 0:
                return False
            return is_power(n/3)

        return(is_power(n))

# Time: O(log(3) N)
# Space: O(log(3) N)