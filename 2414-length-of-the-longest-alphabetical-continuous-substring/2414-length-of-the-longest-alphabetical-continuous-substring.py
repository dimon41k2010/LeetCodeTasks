class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        index_dict = {}
        for i in range(len(alphabet)):
            index_dict[alphabet[i]] = i

        def max_match(s,i,alphabet):
            j = index_dict[s[i]]
            res = 0
            while i < len(s) and j < len(alphabet) and s[i] == alphabet[j]:
                res += 1
                j += 1
                i += 1
            return res
        
        i = 0
        res = 0
        while i < len(s):
            sub_res = max_match(s,i,alphabet)
            res = max(sub_res, res)
            i += sub_res
        return(res)

#Time: O(N)
#Space: O(1)