class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        while left < len(nums) and right >= 0 and nums[left] <= nums[right]:
            mid = (left + right) // 2
            if target == nums[mid]:
                return (mid)
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return (-1)

# Time: O(log N) Binary search
# Space: O(1)