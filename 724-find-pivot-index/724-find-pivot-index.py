class Solution:
    def pivotIndex(self, nums: List[int]) -> int:  
        
        n = len(nums)                                           
        sum_list = []                             
        sum_list.append(0)
        for i in range(0, n):                      # O(n)
            sum_list.append(sum_list[i] + nums[i])

        for i in range(0, n):                      # O(n)
            sum_l = sum_list[i]
            sum_r = sum_list[n] - sum_list[i + 1] 
            if sum_l == sum_r:
                return i
             
        return -1
    
    # Time: O(n)
    # Space: O(1)