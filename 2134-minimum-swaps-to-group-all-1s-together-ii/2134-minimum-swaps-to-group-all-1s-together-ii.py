class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ones = nums.count(1)    # Time: O(N)
        nums = nums + nums
        ones_in_window = 0
        res = 0
        for i in range(len(nums)):      # Time: O(N)
            if i >= ones:
                ones_in_window -= nums[i - ones]
            ones_in_window += nums[i]
            res = max(ones_in_window, res)

        return (ones - res)

# Time: O(N) + O(N)
# Space: O(2 * N) = O(N)
