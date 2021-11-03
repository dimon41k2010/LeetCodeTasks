class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # d = Counter(arr)
        # res = -1
        # for key in d.keys():   # O(N)
        #     if key == d[key]:
        #         if res < key:
        #             res = key
        # return(res)

# Time:  O(N)
# Space: O(N)

# ===== 2nd solution
        dict = Counter(arr)
        res_candidates = [ key for key in dict.keys() if key == dict[key] ]
        res_candidates.append(-1)
        return ( max(res_candidates) )

# Time:  O(N)
# Space: O(N)