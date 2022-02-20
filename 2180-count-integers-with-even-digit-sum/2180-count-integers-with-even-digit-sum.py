class Solution:
    def countEven(self, num: int) -> int:
        
        def is_valid(num): #999
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res % 2 == 0

        res = 0
        for n in range(1, num+1):
            if is_valid(n):
                res += 1
        return (res)

        
# Time: O(N * M) // N->numbers in range n, M->length of num
# Space: O(1)