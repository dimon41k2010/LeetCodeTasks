class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]

        for i in range(1, len(nums)):
            dp_res = 0

            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp_res = max(dp_res, dp[j])
            dp.append(dp_res+1)
        return max(dp)