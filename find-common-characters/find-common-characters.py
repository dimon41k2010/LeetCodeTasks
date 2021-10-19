class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = set()
        for word in words:
            for letter in word:
                letters.add(letter)
        res = []
        for unique_letter in letters:
            counter = words[0].count(unique_letter)
            for word in words:
                counter = min(counter, word.count(unique_letter))
            for i in range(counter):
                res.append(unique_letter)
        return (res)

#Time: O(N * W) + O(26 * N * 2W) = O(N * W)
#Space: O(26)