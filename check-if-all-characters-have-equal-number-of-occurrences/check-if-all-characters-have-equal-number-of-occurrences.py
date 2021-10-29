class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        print(d)

        return (len(set(d.values())) == 1)
#Time: O(N)
#Space: O(26) + O(26)
        