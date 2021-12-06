class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        def is_power(n):
            if n == 1:
                return True
            
            if n % 2 != 0:
                return False
            n /= 2
            return is_power(n)

        return (is_power(n))

# Time: O(log N)
# Space: O(log N)