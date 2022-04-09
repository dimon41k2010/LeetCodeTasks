class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        for _ in range(n-1):
            for i in range(1, len(nums)):
                nums[i-1] = (nums[i-1] + nums[i]) % 10
            nums.pop()
          
        return nums[0]
    
    
# Time: O(N^2)
# Space: O(N)