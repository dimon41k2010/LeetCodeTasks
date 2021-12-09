class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        S = "0"

        def invert(s):  #Time: O(len(s))
            res = []
            for val in s:
                if val == "0":
                    res.append("1")
                else:
                    res.append("0")
            return "".join(res)
        # print(invert("0111001"))

        def reverse(s):     #Time: O(len(s))
            return s[::-1]

        for i in range(1, n):       #Time: O(N * 2^N)
            S = S + "1" + reverse(invert(S))
        return (S[k-1])

#Time: O(N * 2^N)
#Space: O(2^N)

# need to come back and read