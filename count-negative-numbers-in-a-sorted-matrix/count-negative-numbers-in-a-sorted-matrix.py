class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        def count(arr):                # Time: (log C)
            left, right = 0, len(arr)-1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] >= 0:  # Green zone
                    left = mid + 1
                elif arr[mid] < 0:  # Red zone
                    right = mid - 1
            return len(arr)-left

        return ( sum( [count(raw) for raw in grid] ))   # Time: R * (log C)

# Time: R * (log C) + O(R) = R * (log C)
# Space: O(R) // R = raw