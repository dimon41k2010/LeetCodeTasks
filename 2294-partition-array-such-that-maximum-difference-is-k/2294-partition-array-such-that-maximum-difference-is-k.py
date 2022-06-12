class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        res, i = 0, 0
        while i < len(nums):
            start_val = nums[i]
            while i < len(nums) and nums[i] - start_val <= k:
                i += 1
            res += 1
        return (res)

    
#Time: O(N Log N) + O(N) => O(N Log N)
#Space: O(1)