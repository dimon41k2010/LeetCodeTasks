class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        begin_group = 0
        n = len(s)
        res = []
        for i in range(1, n):
            if s[i-1] == s[i]:
                pass
            else:
                lenght = i - begin_group
                if lenght >= 3:
                    res.append([begin_group, i-1])
                begin_group = i

        if s[begin_group] == s[n - 1] and n - begin_group >= 3:
            res.append([begin_group, n - 1])

        return res

# Time: O(N)
# Space: O(1)