class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums, left, right, calc):
        
            if left+1 == right:
                return calc(nums[left], nums[right])

            mid = (left + right) // 2
            left_res = helper(nums, left, mid, min)
            right_res = helper(nums, mid+1, right, max)
            return calc(left_res, right_res)

        return helper(nums, 0, len(nums)-1, min)

    
    
#Time: O(N*2) -> O(N)
#Space: O(Log N)