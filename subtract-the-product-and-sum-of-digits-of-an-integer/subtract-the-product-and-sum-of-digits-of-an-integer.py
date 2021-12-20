class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
# iterative solution
        def product(n):
            res = 1
            while n != 0:
                digit = n % 10
                res *= digit
                n = n // 10

            return res

        def sum(n):
            res = 0
            while n != 0:
                digit = n % 10
                res += digit
                n = n // 10

            return res

        return(product(n) - sum(n))

#Time: O(Log N) + O(Log N) => O(Log N)
#Space: O(1)