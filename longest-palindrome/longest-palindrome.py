class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = {}
        for val in s:
            if val in d.keys():
                d[val] += 1
            else:
                d[val] = 1
        
        res = 0
        is_odd = False
        for key in d.keys():
            if d[key] >= 2:         
                res += d[key] - (d[key] % 2)
            if d[key] % 2 == 1:
                is_odd = True
        if is_odd:
            res += 1

        return res

# Time: O(n) + O(26+26) = O(n)
# Space: O(26+26) + O(1) = O(1)