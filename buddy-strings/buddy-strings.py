class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        # for i in range(len(s)):
        #     for j in range(i+1,len(s)):
        #         s_list = list(s)
        #         s_list[i], s_list[j] = s_list[j], s_list[i]
        #         # word = s[0:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        #    #            ''    +  'a' +   'b'    +  'd' +   'c'
        #         if ''.join(s_list) == goal:
        #             return ( True )
        #         # if word == goal:
        #         #     return (True)
        # return (False)

        
#Time: O(N^3)
#Space: O(N)


        list_inx = []           #O(2) due to written conditions
        if len(s) != len(goal):
            return(False)

        for i in range(len(s)):
            if s[i] == goal[i]:
                pass
            else:
                list_inx.append(i)
                if len(list_inx) > 2:
                    return(False)

        if len(list_inx) == 2:
            i, j = list_inx
            if s[i] == goal[j] and s[j] == goal[i]:
                return(True)
        if len(list_inx) == 0:
            if len(set(s)) != len(s):
                return(True)
        return(False)

#Time: O(N + M)
#Space: O(N) + O(2)