class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         start = 0
#         res = 0
#         for i in range(0, len(nums)):
#             if nums[i] == 0:
#                 start = i+1
#             res = max(res, i-start + 1) 

#         return res
    
# Time: O(n) +  O(1) = O(n)
# Space: O(1)

            count = maxCount = 0

            for i in range(len(nums)):
                if nums[i] == 1:
                    count += 1
                else:
                    maxCount = max(count, maxCount)
                    count = 0

            return max(count, maxCount)