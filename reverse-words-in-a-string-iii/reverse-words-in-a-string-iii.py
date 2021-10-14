class Solution:
    def reverseWords(self, s: str) -> str:
        index = 0
        res = []
        while index < len(s):
            word = []
            while index != len(s) and s[index] != ' ':
                word.append(s[index])      #Time: O(1) / O(n)   #Space: O(n)
                index += 1

            res.append("".join(word[::-1])) #Time: O(n) / O(1) 

            if index != len(s):
                res.append(" ")
            index += 1

        return ("".join(res))

# Time: O(n)
# Space: O(n)