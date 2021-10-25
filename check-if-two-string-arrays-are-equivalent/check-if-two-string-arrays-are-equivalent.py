class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_char = []
        for i in range(len(word1)):
            for j in range(len(word1[i])):      # O(N1*W1)
                word1_char.append(word1[i][j])

        inx = 0
        for i in range(len(word2)):
            for j in range(len(word2[i])):      # O(N2*W2)
                if inx >= len(word1_char) or word2[i][j] != word1_char[inx]:
                    return(False)
                inx += 1
        return (inx == len(word1_char))

#Time: O(N1*W1) + O(N2*W2)
#Space: O(N)  // N = len(N1)


#Second solution with Space: O(1)
#         i, j = 0, 0
#         for sub_word in word1:
#             for letter in sub_word:
#                 if i == -1 or letter != word2[i][j]:
#                     return False
#                 i, j = next_(word2, i, j)
#         return i == -1

# def next_(word, i, j):
#     if j < len(word[i]) - 1:
#         return i, j + 1
#     if i < len(word) - 1:
#         return i + 1, 0
#     return -1, -1
