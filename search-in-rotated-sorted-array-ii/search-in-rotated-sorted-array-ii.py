class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        def binary_search(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if target == nums[mid]:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
            return False

        def binary_search_mod(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                print(left, mid, right)
                if target == nums[mid]:
                    return True
                if nums[left] == nums[mid] : # Fail to estimate which side is sorted
                    left += 1
                    continue
                if nums[right] == nums[mid] : # Fail to estimate which side is sorted
                    right -= 1
                    continue
                if target <= nums[-1]:  # Target in red (right side)
                    if nums[mid] <= nums[-1]:  # Mid in red
                        if target < nums[mid]:
                            right = mid - 1
                        elif nums[mid] < target:
                            left = mid + 1
                    else:                     # mid in green
                        left = mid + 1
                else:                   # Target in green (left side)
                    if nums[mid] <= nums[-1]:   # Mid in red
                        right = mid - 1
                    else:  # Mid in green
                        if target < nums[mid]:
                            right = mid - 1
                        else:
                            left = mid + 1
            return False

        return (binary_search_mod(nums, target) or binary_search(nums, target))

# Time: O(log N) Binary search
# Space: O(1)