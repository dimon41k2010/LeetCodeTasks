class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        count = 1

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            res = max(res, count)
        return (res)

#Time: O(N)
#Space: O(1)