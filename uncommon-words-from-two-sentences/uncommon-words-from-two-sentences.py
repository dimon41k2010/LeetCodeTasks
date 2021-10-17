class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()  #O(N) + O(M)
        d = {}
        for word in words:              # O(N)
            if word in d.keys():
                d[word] += 1
            else:
                d[word] = 1

        res = []
        for key in d.keys():
            if d[key] == 1:
                res.append(key)
        return(res)

#Time: O(N) + O(M) 
#Space: O(N) + O(M) 