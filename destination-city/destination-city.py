class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for val in paths:
            s.add(val[0])
        # print(s)
        for i in range(len(paths)):
            if paths[i][1] not in s: #O(1)
                # print(paths[i][1])
                # break
                return paths[i][1]
            
            
#Time: O(N) + O(1) + O(N) = O(N)
#Space: O(N * W) = O(N)  //  W=len(paths[i][1])