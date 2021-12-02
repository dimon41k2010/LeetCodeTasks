class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif target <= nums[mid]:
                    right = mid - 1
            return left
        nums.sort()
        index = binary_search(nums, target)
        res = []
        while index < len(nums) and nums[index] == target:   #Time: O(N) 
            res.append(index)
            index += 1
        return (res)

# Time: O(log N) -> Binary search + O(N) -> worse case
# Space: O(1)