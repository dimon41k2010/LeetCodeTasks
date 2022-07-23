class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        i = 0
        res = 0
        while i < len(nums):
            len_ = 0
            while i < len(nums) and nums[i] == 0:
                len_ += 1
                i += 1

            res += len_ * (len_ + 1) // 2
            i += 1

        return (res)

#Time: O(N) 
#Space: O(1)