class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for pattern in patterns:
            if pattern in word:
                res += 1
        return (res)

#Time: O(N * W)
#Space: O(1)

        # return ([ (p in word) for p in patterns].count(True))