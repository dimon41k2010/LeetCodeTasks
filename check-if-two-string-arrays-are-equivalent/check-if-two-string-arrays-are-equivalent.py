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