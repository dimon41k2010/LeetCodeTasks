class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        max_diff = -1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    diff = abs(nums[i] - nums[j])
                    max_diff = max(diff, max_diff)

        return max_diff