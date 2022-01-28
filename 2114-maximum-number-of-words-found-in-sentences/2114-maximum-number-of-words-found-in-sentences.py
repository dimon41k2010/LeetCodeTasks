class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        return max([len(sentence.split(" ")) for sentence in sentences])


# Time: O(N * S) // N=numbers of sentences, S=numbers of characters in sentence
# Space: O(N + S) // N=numbers of sentences, S=numbers of characters in sentence