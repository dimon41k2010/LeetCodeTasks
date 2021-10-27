class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        lst = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                lst.append(i)
        if len(lst) > 2 or len(lst) == 1:
            return (False)
        if len(lst) == 2 and s1[lst[0]] == s2[lst[1]] and s2[lst[0]] == s1[lst[1]]:
            return (True)
        if len(lst) == 0:
            return (True)
        return (False)

#Time: O(N + M) 
#Space: O(N)