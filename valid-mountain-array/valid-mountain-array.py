class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        is_peak = False
        for i in range(1, len(arr)):
            if is_peak:                 # red zone
                if arr[i-1] > arr[i]:
                    pass
                elif arr[i-1] <= arr[i]: # Transition or equal: Red -> Green = False
                    return (False)
                    
            elif not is_peak:           # green zone
                if arr[i-1] > arr[i]:   # Transition: Green -> Red
                    if i == 1:
                        return False
                    is_peak = True
                elif arr[i-1] < arr[i]: 
                    pass
                elif arr[i-1] == arr[i]:
                    return (False)
    
        return (is_peak)

# Time: O(N)
# Space: O(1)