class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        set_ = set(nums)
        res = -1
        for num in nums:
            if num > 0 and -num in set_:
                res = max(res, num)
        return(res)

#Time: O(N)
#Space: O(N)