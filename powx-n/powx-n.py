class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        memo = {}
        def pow_f(x, n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n == 1:
                return x
            if n == -1:
                return 1/x
            if n % 2 != 0:
                memo[n] = x * pow_f(x * x, n // 2)
                return memo[n]

            memo[n] = pow_f(x * x, n // 2)
            return memo[n]
        
        return (pow_f(x, n))
    

#Time: O(log N)
#Space: O(log N)