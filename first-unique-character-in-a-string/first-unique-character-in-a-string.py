class Solution:
    def firstUniqChar(self, s: str) -> int:

        res = len(s)
        for i in set(s): # O(26)
            if s.count(i) == 1:  # O(n)
                res = min(res, s.index(i))   

        if res == len(s): 
            return -1
        else:
            return res

        # Time: O(n)
# Space: O(26) = O(1)