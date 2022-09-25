class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = 100000
        res = []
        dic = {}
        for i in range(len(heights)):
            dic[heights[i]] = names[i]

        for num in range(n,0,-1):
            if num in dic.keys():
                res.append(dic[num])
        return (res)
    
    
    
#         new_heights = sorted(heights, reverse=True)
#         new_res = []
#         dic_new = {}
#         for i in range(len(heights)):
#             dic_new[heights[i]] = names[i]

#         for val in new_heights:
#             new_res.append(dic_new[val])
#         return (new_res)
