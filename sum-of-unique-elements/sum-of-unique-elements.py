class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
#         d = {}
#         for i in range(len(nums)):
#             if nums[i] not in d.keys():
#                 d[nums[i]] = 1
#             else:
#                 d[nums[i]] += 1

#         return(sum( [key for key in d.keys() if d[key] == 1]))
        
#Time: O(N) // N -> len(nums)
#Space: O(N)

# one-liner / list comprehension with count()

            return sum([num for num in nums if nums.count(num) == 1])
