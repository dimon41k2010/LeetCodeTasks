class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res += nums[i]

        return res
       
    # Time: O(N log N) + O(n) = O(N log N)
    # Space: O(1)