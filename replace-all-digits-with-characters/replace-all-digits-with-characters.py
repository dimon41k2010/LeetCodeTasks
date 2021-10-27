class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if i % 2 == 0:
                res.append(s[i])
            else:
                res.append(chr(ord(s[i-1]) + int(s[i])))
        return (''.join(res))

#Time: O(N)
#Space: O(N)