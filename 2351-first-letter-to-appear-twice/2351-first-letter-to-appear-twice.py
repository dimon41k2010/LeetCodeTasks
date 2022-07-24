class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        dic = {}
        for char in s:
            if char not in dic.keys():
                dic[char] = 1
            else:
                return(char)

        # set_ = set()
        # for char in s:
        #     if char not in set_:
        #         set_.add(char)
        #     else:
        #         return(char)

#Time: O(N)
#Space: O(1)