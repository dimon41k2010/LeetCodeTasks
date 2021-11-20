class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = [] 
        if len(nums) == 0: 
            return res
        start = nums[0]
        temp_s = ''
        
        for i in range(0, len(nums)):
            if i + 1 >= len(nums) or nums[i] + 1 != nums[i+1]:
                temp_s = str(start)
                if start != nums[i]:
                    temp_s += "->" + str(nums[i])
                if i+1 < len(nums):
                    start = nums[i+1]
                res.append(temp_s)
        
        return res

    # Time: O(n)
    #Space: O(1)