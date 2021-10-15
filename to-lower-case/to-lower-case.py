class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        for char in s:
            if ord(char) in range(65, 91):
                res.append(chr( ord(char) + 32 ))
            else:
                res.append(char)
        return "".join(res)

# Time: O(n) + O(n) = O(n)
# Space: O(n)

        #=============
        # res1 = ''
        # for char in s:
        #     if ord(char) in range(65, 91):
        #         res1 += (chr( ord(char) + 32 ))
        #     else:
        #         res1 += char
        # return (res1)

# Time: O(n2)
# Space: O(1)