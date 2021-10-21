class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        d={}
        for i in range(len(chars)):
            if chars[i] in d.keys():
                d[chars[i]] += 1
            else:
                d[chars[i]] = 1
        # pattern: "is_Flag"
        for word in words:              #O(N)
            temp_d = d.copy()
            is_add = True
            for char in word:  
                if char in temp_d.keys():
                    if temp_d[char] == 0:
                        is_add = False
                        break
                    temp_d[char] -= 1
                else:
                    is_add = False
                    break
            if is_add:
                res += len(word)
        return (res)

#Time: O(C) + O(N * W) = O(N * W) // N=len(words)  W=len(word)
#Space: O(N) // N=26 letters  => O(1)