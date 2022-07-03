class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        dic = {}
        for word in words2:
            if word not in dic.keys():
                dic[word] = 1
            else:
                dic[word] += 1
        # print(dic)

        dic1 = {}
        for word in words1:
            if word not in dic1.keys():
                dic1[word] = 1
            else:
                dic1[word] += 1
        # print(dic1)
        res = 0
        for key in dic1.keys():
            if dic1[key] == 1:
                if key in dic.keys():
                    if dic[key] == 1:
                        res += 1
        return(res)
    