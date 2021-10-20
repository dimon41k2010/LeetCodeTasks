class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()    #O(N)
        res = []
        for i in range(len(words)-2):  #O(N)
            if words[i] == first and words[i+1] == second:
                res.append(words[i+2])
        return (res)

#Time: O(C) + O(N * W) / W=len(words), C=len(chars)
#Space: O(C)