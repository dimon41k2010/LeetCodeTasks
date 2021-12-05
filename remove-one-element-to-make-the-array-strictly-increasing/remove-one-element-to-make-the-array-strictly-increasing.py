class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
#         for i in range(len(nums)):
#             temp = list(nums)
#             temp.pop(i)
#             if temp == sorted(temp) and len(temp) == len(set(temp)):
#                 return (True)
            
#         return(False)
    
# Time: O(N^2) -> due to temp list creation on every iteration 
# Space: O(N + M)


# == Second Better solution
        def is_sorted(arr):                 # Time: O(N)
            for i in range(1, len(arr)):
                if arr[i-1] >= arr[i]:
                    return False
            return(True)

        for i in range(1, len(nums)):       # Time: O(N)
            if nums[i-1] >= nums[i]:
                return (is_sorted(nums[0:i-1] + nums[i:]) or is_sorted(nums[0:i] + nums[i+1:]))
        return (True)

# Time: O(5 * N) = O(N)
# Space: O(N)