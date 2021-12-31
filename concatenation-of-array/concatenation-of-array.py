class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [ -1 for _ in range(2 * len(nums)) ]

        for i in range(len(nums)):
            n = len(nums)
            ans[i], ans[i+n] = nums[i], nums[i]
        return (ans)
    
# Time: O(N)
# Space: O(N)

# Pythonic
        return nums * 2

# Time: O(N)
# Space: O(1)