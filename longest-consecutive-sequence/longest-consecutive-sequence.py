class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        set_nums = set(nums)
        count = 0
        
        for num in nums:
            if num-1 not in set_nums:
                segment = 1
                while num+1 in set_nums:
                    segment += 1
                    num += 1
                
                count = max(segment, count)
        return (count)
    
# Time: O(N)
# Space: O(N)