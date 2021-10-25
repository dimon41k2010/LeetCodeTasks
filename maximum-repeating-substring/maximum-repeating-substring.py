class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        res = 0
        for i in range(len(sequence)):
            count = 0
            j = i
            while j + len(word) <= len(sequence) and sequence[j : j + len(word)] == word:
                count += 1
                j += len(word)
            res = max(count, res)
        return (res)

#Time: O(N^2)
#Space: O(1)
        