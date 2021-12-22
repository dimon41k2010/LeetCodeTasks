class Solution:
    def sumBase(self, n: int, k: int) -> int:
    
# recursion
        def solve(n, k):
            # print("Enter", toStr(n, k))
            if n == 0:
                return 0
            # print(n % k)
            res = n % k
            res += solve(n // k, k)
            # print("Exit", toStr(n, k), res)
            return res

        return solve(n, k)

#Time: O(Log(k) N)
#Space: O(Log(k) N)


# iterative 
        res = 0
        while n > 0:
            res += n % k
            n = n // k
        return res

#Time: O(Log(k) N)
#Space: O(1)