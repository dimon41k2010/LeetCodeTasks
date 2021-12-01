class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        def is_valid(arr, number, d):                # Time: (log C)
            left, right = 0, len(arr)-1
            start_red, end_red = number - d, d + number
            while left <= right:
                mid = (left + right) // 2
                if start_red <= arr[mid] and arr[mid] <= end_red:  # Red zone
                    return False

                elif arr[mid] < start_red :        # Green zone
                    left = mid + 1
                elif end_red < arr[mid]:           # Yellow zone
                    right = mid - 1
            return True

        arr2.sort()
        return(sum ([ 1 for val in arr1 if is_valid(arr2, val, d ) ]))