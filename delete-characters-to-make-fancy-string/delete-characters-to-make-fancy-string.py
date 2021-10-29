class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for val in s:
            if len(res) < 2 or res[-1] != val or res[-2] != val:
                res.append(val)
        return ("".join(res))

#Time: O(N)
#Space: O(N)