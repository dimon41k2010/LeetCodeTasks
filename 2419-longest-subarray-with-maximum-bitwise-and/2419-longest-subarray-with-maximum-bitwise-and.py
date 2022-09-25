class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
#        3 011
#        2 010
#        1 001
        
#         4 010 
#         5 000
        
    
        max_num = max(nums)
        count_max_num = 0
        res = 0
        for num in nums:
            if num == max_num:
                count_max_num += 1
            else:
                count_max_num = 0

            res = max(count_max_num, res)
        return (res)

#Time: O(N) 
#Space: O(1)