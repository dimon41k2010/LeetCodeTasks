class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        d = {}
        
        def is_valid(d,k):
            return sum(d.values()) - max(d.values()) <= k

        index = 0
        res = 0
        for char in s:
            if char not in d.keys():
                d[char] = 1
            else:
                d[char] += 1
            while not is_valid(d,k):
                c = s[index]
                index += 1
                d[c] -= 1
            res = max(res, sum(d.values()))

        return (res)

#Time: O(N)
#Space: O(1)
         