class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        for i in range(len(strs[0])): #
            is_success = True
            for k in range(1, len(strs)):
                if i >= len(strs[k]) or strs[k][i] != strs[k-1][i]:
                    is_success = False
                    break
            if is_success:
                res += strs[0][i]
            else:
                break
        return res
    

#Time: O(n) * O(m) = O(n2) // n=len(strs) m=len(strs[0])
#Space: O(1)