class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         if nums[0] != 0:
#             return 0
#         for i in range(1, len(nums)):
#             if nums[i-1] != nums[i] - 1:
#                 return nums[i]-1

#         return len(nums)
    
    # Time: O(N log n) + O(n) = O(N log n)
    #Space: O(1)
    
    
        # s = set(nums)
        s = set()
        for val in nums:
            s.add(val)
        for val in s:
            if val == 0:
                continue
            if val-1 not in s:
                return val-1
        return len(nums)
    
    # Time: O(n)
    #Space: O(n)