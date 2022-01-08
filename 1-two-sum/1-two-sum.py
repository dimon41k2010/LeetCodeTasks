class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   
  
    #1. Brute force 0(N^2) Time, 0(1) Space

        if not nums or len(nums) < 2:
            return[]
        
        seen = {}
        for i in range(len(nums)):
            numNeeded = target - nums[i]
            if numNeeded in seen:
                return [i, seen[numNeeded]]
            else:
                seen[nums[i]] = i 
   
    # USE THIS ONE -- Method 2. 0(N) Time, 0(N) Space 

        if not nums or len(nums) < 2:
            return[]
        
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            tempSum = nums[left] + nums[right]
            
            if tempSum == target:
                return[nums[left], nums[right]]
            elif tempSum < target:
                left += 1
            else: 
                right -= 1
                
        return[]
