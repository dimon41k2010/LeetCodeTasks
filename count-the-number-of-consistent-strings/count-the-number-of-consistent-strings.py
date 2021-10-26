class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_s = set(allowed)
        res = 0
        for word in words:
            res += 1
            for letter in word:
                if letter not in allowed_s:
                    res -= 1
                    break
        return (res)

#Time: O(N * W)
#Space: O(N) // N=26 