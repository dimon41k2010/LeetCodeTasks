class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        index = 0
        res = ''
        while index < len(s):
            first = s[index:k+index][::-1]

            second = s[index+k: index+k*2]

            res += first + second
            index += 2 * k
        return res