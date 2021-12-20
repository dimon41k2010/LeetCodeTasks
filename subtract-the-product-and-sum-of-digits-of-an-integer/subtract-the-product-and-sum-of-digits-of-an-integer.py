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


#===== Recursion solution
        def product_recur(n):
            if n == 0:
                return 1

            digit = n % 10

            return digit * product_recur(n // 10)

        def sum_recur(n):
            if n == 0:
                return 0

            digit = n % 10

            return digit + sum_recur(n // 10)

        return (product_recur(n) - sum_recur(n))

#Time: O(Log N) + O(Log N) => O(Log N)
#Space: O(Log N) + O(Log N) => O(Log N)

