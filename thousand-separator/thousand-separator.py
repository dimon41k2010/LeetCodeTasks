class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        def int_to_str(numb):
            if numb < 10:
                return "00" + str(numb)
            elif numb < 100:
                 return "0" + str(numb)
            else:
                return str(numb)
            
        res =[]
        while n > 0:
            numb_mod = n % 1000
            n //= 1000
            if n > 0:
                res.append(int_to_str(numb_mod))
            else:
                res.append(str(numb_mod))
            if n > 0:
                res.append(".")
        return "".join(res[::-1])

#Time: O(N) // N=len(n)
#Space: O(N) 


# print(123456789 % 1000)
# print(123456789 // 1000)