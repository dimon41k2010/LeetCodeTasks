class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        res = ""
        index_a = len(a)-1
        index_b = len(b)-1
        carry = 0

        for i in range(max_len -1,-1,-1):
            val = carry
            carry = 0
            if index_a >= 0 and a[index_a] == "1":
                val += 1
            if index_b >= 0 and b[index_b] == "1":
                val += 1
            if val >= 2:
                val = val % 2
                carry = 1
            print(val,' ', carry, ' ', i, ' ', index_a, ' ', index_b)
            res += str(val)
            index_a -= 1
            index_b -= 1
            if i == 0 and carry > 0:
                res += str(carry)

        return res[::-1]
    
    
#Time: O(max(n, m))
#Space: O(1)