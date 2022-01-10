class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = -100000
        sum = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            if sum > res:
                res = sum
            if sum < 0:
                sum = 0
        
        return res
    
    #Time: O(n) 
    #Space: O(1)