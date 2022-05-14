class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        left = nums[0]
        right = sum(nums) - left
        value = sum(nums) + 10000
        res = -1
        
        for i in range(1, len(nums)+1):
            right_side = 0 if len(nums)-i == 0 else right // (len(nums)-i)
            candidate = abs((left // i) - right_side)

            if value > candidate:
                res = i-1
                value = candidate
            
            if i < len(nums):
                left += nums[i]
                right -= nums[i]

        return res

#Time: O(N)
#Space: O(1)