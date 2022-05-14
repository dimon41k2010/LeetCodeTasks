class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # O(N)
        left = nums[0]
        right = total_sum - left
        res = 0
        for i in range(1, len(nums)):
            if left >= right:
                res += 1
            left += nums[i]
            right -= nums[i]
        return res

#Time: O(N)
#Space: O(1)