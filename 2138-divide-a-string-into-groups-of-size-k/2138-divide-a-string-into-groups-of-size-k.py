class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        i = 0
        res = []
        while i < len(s):
            end = min(i+k, len(s))
            sub_string = []
            for j in range(i, end):
                sub_string.append(s[j])
            while len(sub_string) < k:
                sub_string.append(fill)
            res.append("".join(sub_string))
            i += k

        return (res)

# Time: O(N)
# Space: O(N) // N = k or N = len(s)