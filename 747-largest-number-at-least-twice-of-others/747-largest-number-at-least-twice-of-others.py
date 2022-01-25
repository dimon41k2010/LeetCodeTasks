class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        bigest_int_index = 0

        if len(nums) <= 1:
            return 0
        for i in range(0, len(nums)):   # O(n) | Space: O(1) + O(n)
            if nums[bigest_int_index] < nums[i]:    # nums = [3,4,1,0,9]
                bigest_int_index = i

        print(bigest_int_index)
        for i in range(0, len(nums)): 
            if i  == bigest_int_index:
                continue
            if nums[bigest_int_index] / 2 < nums[i]:
                return -1
        
        return bigest_int_index
        
    #Time: O(n)
    #Space: O(1)
    
    
    # solution 2nd
    
        if len(nums) <= 1:
            return 0
        b_i = p_b_i = -1              # b_i = 0 | p_b_i = 1 
        for i in range(0, len(nums)):                 
            if b_i == -1:
                b_i = i 
            elif nums[b_i] <= nums[i]:   
                p_b_i = b_i
                b_i = i
            elif p_b_i == -1:
                p_b_i = i
            elif nums[p_b_i] < nums[i]:
                p_b_i = i
        if nums[b_i] >= nums[p_b_i] * 2: 
            return b_i
        return -1
    
    
    #Time: O(n)
    #Space: O(1)