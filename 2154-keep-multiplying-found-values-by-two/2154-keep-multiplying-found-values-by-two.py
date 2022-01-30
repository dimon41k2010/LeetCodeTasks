class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        set_nums = set(nums)
        while original in set_nums:
            original *= 2
        return original

# Time: O(N)
# Space: O(N)