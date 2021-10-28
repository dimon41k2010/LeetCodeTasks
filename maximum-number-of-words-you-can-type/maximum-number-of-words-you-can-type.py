class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters_set = set(brokenLetters)
        words = text.split()
        res = len(words)
        for word in words:
            for char in word:
                if char in brokenLetters_set:
                    res -= 1
                    break
        return (res)

#Time: O(N)
#Space: O(N)