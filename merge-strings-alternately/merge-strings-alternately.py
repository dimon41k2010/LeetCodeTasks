class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        i_1 = 0
        i_2 = 0
        while i_1 < len(word1) or i_2 < len(word2):
            if i_1 < len(word1):
                res.append(word1[i_1])
            if i_2 < len(word2):
                res.append(word2[i_2])
            i_1 += 1
            i_2 += 1
        return(''.join(res))

#Time: O(N + M) 
#Space: O(N + M)