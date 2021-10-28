class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) == 3:
                res += 1
        return (res)

#Time: O(N)
#Space: O(1)

#Second one-liner
# return(sum([1 if len(set(s[i:i+3])) == 3 else 0 for i in range(len(s)-2)]))

#Time: O(N) + O(N)
#Space: O(N)