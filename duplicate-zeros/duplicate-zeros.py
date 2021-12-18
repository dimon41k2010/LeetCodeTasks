class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0

        return(arr)

#Time: O(N)
#Space: O(1)
        
        
        
        active_zero = 0
        for i in range(len(arr)):
            if arr[i] == 0 :
                active_zero += 1
            if i >= len(arr) - active_zero:
                break

        i = len(arr) - 1
        while i >= 0:
            lookup_index = i - active_zero
            if arr[lookup_index] != 0:
                arr[i] = arr[lookup_index]
                i -= 1
            elif arr[lookup_index] == 0:
                arr[i-1] = 0
                arr[i] = 0
                active_zero -= 1
                i -= 2

        return (arr)

    
#Time: O(N) + O(N)
#Space: O(1)

