class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
#         max_diff = -1
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] < nums[j]:
#                     diff = abs(nums[i] - nums[j])
#                     max_diff = max(diff, max_diff)

#         return max_diff
    
    
#Time: O(N*N)
#Space: O(1)


        maxDiff = -1
        minNumber = nums[0]
        for i in range(len(nums)):
            maxDiff = max(maxDiff, nums[i]-minNumber)
            minNumber = min(nums[i], minNumber)
        
        if maxDiff == 0:
            return (-1)
        
        return maxDiff