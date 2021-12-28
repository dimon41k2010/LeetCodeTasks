class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return (nums[0])

        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            dp.append( max(dp[i-1], dp[i-2] + nums[i]) )
        return dp[-1]
    
    
# Time: O(N)
# Space: O(N)