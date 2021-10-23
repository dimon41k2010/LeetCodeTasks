class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        def count_chars(s, ch):
            count = 0
            for c in s:
                if ch == c:
                    count += 1
            return count
# print(count_chars(s, "1"))
        res = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            score = count_chars(left, "0") + count_chars(right, "1")
            if score > res:
                res = score

        return (res)
    
#Time:
#Space: