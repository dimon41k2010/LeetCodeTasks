class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #nums = [1,0,0,0,3,12]
        
        # ind = 0
        # for i in range(0,len(nums)): 
        #     if nums[i] != 0:
        #         temp = nums[ind]  
        #         nums[ind] = nums[i]  #Talk about this part
        #         nums[i] = temp
        #         #nums[ind], nums[i] = nums[i], nums[ind]
        #         ind += 1
        
        
   
        c=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[c],nums[i]=nums[i],nums[c]
                c+=1
        return nums        

        
       