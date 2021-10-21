class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = {}
        for i in range(1,27):
            key = str(i)
            if i >= 10:
                key += "#"
            d[key] = chr(ord("a") + i - 1)
        res = []
        i = len(s)-1
        while i >= 0:           #O(N)
            if s[i] == "#":
                key = s[i-2:i+1]
                i -= 3
                res.append(d[key]) 
            else:
                key = s[i]
                res.append(d[key])
                i -= 1
        return ("".join(res[::-1]))  #O(N)

#Time: O(1) + O(N) + O(N) = O(N)
#Space: O(1) + O(N)