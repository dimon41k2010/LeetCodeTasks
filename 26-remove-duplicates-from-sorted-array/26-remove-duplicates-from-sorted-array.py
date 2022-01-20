class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        index_unique = 1
        for i in range(1, len(nums)): 
            if nums[i] != nums[i-1]:
                nums[index_unique] = nums[i]
                index_unique += 1
       
        return index_unique    
                
# Time: O(N)
# Space: O(1)