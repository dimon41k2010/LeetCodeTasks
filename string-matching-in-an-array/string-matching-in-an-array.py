class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    res.add(words[i])
        return list(res)

#Time: O(N^2 * W) / W=len(word)
#Space: O(1)