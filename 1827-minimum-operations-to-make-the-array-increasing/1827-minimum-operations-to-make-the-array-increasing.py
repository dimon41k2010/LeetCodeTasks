class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        prev = nums[0]
        res = 0
        for i in range(1, len(nums)):
            if prev >= nums[i]:
                res += prev + 1 - nums[i]
                prev += 1
            else:
                prev = nums[i]
        return (res)

#Time: O(N)
#Space: O(1)