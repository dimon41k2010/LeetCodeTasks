class Solution:
    def minimumMoves(self, s: str) -> int:
        counter = 0
        i = 0
        while i < len(s):
            if s[i] == "X":
                counter += 1
                i += 3
            else:
                i += 1

        return (counter)

#Time: O(N)
#Space: O(1)