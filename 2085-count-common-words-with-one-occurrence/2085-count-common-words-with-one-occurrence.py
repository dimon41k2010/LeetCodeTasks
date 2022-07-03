class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        dic2 = {}
        for word in words2:
            if word not in dic2.keys():
                dic2[word] = 1
            else:
                dic2[word] += 1

        dic1 = {}
        for word in words1:
            if word not in dic1.keys():
                dic1[word] = 1
            else:
                dic1[word] += 1

        res = 0
        for key in dic1.keys():
            if dic1[key] == 1 and key in dic2.keys():
                if dic2[key] == 1:
                    res += 1
        return (res)

#Time: O(N) + O(M)
#Space: O(N) + O(M)
    