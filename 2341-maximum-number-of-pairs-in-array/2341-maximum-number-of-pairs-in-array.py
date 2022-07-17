class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        count_dict = Counter(nums)
        
        res = [0,0]
        for val in count_dict.values():
            if val % 2 != 0:
                res[1] += 1
            res[0] += val // 2

        return (res)

#Time: O(N)
#Space: O(N)