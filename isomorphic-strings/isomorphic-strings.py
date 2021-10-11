class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d.keys():
                if t[i] != d[s[i]]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]

        return True

# Time: O(n+m) = O(n)
# Space: O(n)  // n = ASCII -> 128 => O(1)