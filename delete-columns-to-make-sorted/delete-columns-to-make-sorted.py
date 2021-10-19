class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        C = len(strs[0])
        R = len(strs)
        res = 0

        for c in range(0,C):
            for r in range(1, R):
                val = strs[r][c]
                if val < strs[r-1][c]:
                    res += 1
                    break
        return (res)

#Time: O(C * R)
#Space: O(1)