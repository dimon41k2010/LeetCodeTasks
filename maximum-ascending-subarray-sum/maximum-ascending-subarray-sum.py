class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sub_sum = nums[0]
        max_sub_sum = nums[0]

        for i in range(1, len(nums)):
            if i <= len(nums) and nums[i] <= nums[i-1]:
                sub_sum = nums[i]
            else:
                sub_sum += nums[i]
            max_sub_sum = max(sub_sum, max_sub_sum)

        return (max_sub_sum)

#Time: O(N)
#Space: O(1)