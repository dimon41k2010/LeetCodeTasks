class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        min_ = 1001
        max_ = 0
        for num in nums:
            if num > max_:
                max_ = num
            if num < min_:
                min_ = num

        for candidate in range(min_, 0, -1):
            if max_ % candidate == 0 and min_ % candidate == 0:
                return (candidate)
       

    
# Time: O(N)
# Space: O(1)
        