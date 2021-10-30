class Solution:
    def isHappy(self, n: int) -> bool:
        def transform(num):
            res = 0
            while num > 0:
                digit = num % 10
                res += digit * digit
                num //= 10
            return res

        s = set()
        while n != 1:
            n = transform(n)
            if n in s:
                return(False)
            s.add(n)
        return(True)

#Time: not defined
#Space: O(1)