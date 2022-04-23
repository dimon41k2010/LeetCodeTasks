class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        
        def calc(chunk):
            res = 0
            for char in chunk:
                res += int(char)
            return str(res)

        while len(s) > k:
            chunks = []
            for i in range(0, len(s), k):
                end = min(i+k, len(s))
                chunks.append(calc(s[i:end]))
            s = "".join(chunks)

        return (s)


# Time: O(N log N)
# Space: O(N)