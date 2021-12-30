class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return(max(nums))
        
        def solver(nums):
            
            dp = [ 0 for _ in range(len(nums))]

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            return dp[-1]

        return (max(solver(nums[:-1]),solver(nums[1:])))

# Time: O(2 * N) => O(N)
# Space: O(N)