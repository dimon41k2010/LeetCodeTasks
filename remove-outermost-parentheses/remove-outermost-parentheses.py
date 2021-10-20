class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter=0
        begin = 0
        res = []
        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
            elif s[i] == ")":
                counter -= 1
            if counter == 0:
                res.append(s[begin + 1 : i])
                begin = i + 1
        return ''.join(res)

#Time: O(N)
#Space: O(N)