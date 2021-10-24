class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        chars_dict = {}
        for i in range(len(indices)):     #O(N)
            chars_dict[indices[i]] = s[i]
        res = []
        for i in range(len(indices)):     #O(N)
            res.append(chars_dict[i])
        return(''.join(res))               #O(N)

#Time: O(N)
#Space: O(N) + O(N) 