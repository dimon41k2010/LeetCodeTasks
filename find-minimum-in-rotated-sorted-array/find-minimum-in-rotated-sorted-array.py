class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def binary_search_min(nums):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= nums[-1]:  # Mid in red
                    right = mid - 1
                elif nums[0] <= nums[mid]:  # mid in green
                    left = mid + 1
            return nums[left]

        
        begin = nums[0]
        end = nums[-1]
        if begin > end:
            return(binary_search_min(nums))
        else:
            return(begin)

# Time: O(log N) Binary search
# Space: O(1)