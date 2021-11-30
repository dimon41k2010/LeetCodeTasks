class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            if mid == 0 or arr[mid-1] < arr[mid]:  # Green zone
                left = mid + 1
            elif arr[mid-1] > arr[mid]:  # Red zone
                 right = mid - 1

        return (right)

# Time: O(log N) Binary search
# Space: O(1)