class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
#         if k == 0:
#             return False
#         max_range = k + 1
#         for i in range(0, len(nums)):
#             for j in range(i+1, min(max_range+i, len(nums))):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
    
    
# Time: O(n2)
# Space: O(1)
        
        if k == 0:
            return (False) 
        d = {}
        for i in range(0, len(nums)):
            if nums[i] in d.keys() and i - d[nums[i]] <= k: #1
                return(True)
            else:
                d[nums[i]] = i

        return (False)
    
# Time: O(N)
# Space: O(N)