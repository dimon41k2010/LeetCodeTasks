class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        index = 0
        dic = {}
        for char in key:
            if char != " " and char not in dic.keys():
                dic[char] = index
                index += 1

        res = []
        for char2 in message:
            if char2 == " ":
                res.append(char2)
            else:
                res.append(chr(ord("a") + dic[char2]))

        return ("".join(res))

#Time: O(N) + O(M)
#Space: O(26) + O(M)