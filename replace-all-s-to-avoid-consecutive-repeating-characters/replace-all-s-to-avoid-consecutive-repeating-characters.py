class Solution:
    def modifyString(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            set_ = set()
            if i != 0:
                if s[i-1] == "?":
                    set_.add(res[-1])
                else:
                    set_.add(s[i-1])

            if i != len(s)-1 and s[i+1] != "?":
                set_.add(s[i+1])
            if s[i] == "?":
                for char in "abcde":   #O(5)
                    if char not in set_:  #O(1)
                        res.append(char)
                        break
            else:
                 res.append(s[i])
        return "".join(res)

#Time: O(N)
#Space: O(N)