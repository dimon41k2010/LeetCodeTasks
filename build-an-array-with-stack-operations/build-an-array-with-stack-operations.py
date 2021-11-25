class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        set_target = set(target)    #Space: O(N)
        res_list = []
        count = len(target)         #Space: O(1)
        for i in range(1, n+1):
            res_list.append("Push")
            count -= 1
            if i not in set_target:
                res_list.append("Pop")
                count += 1
            if count == 0:
                break
        return res_list

# Time: O(N)
# Space: O(N)