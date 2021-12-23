class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        num_max = 0
        num_max_second = 0
        num_min = 0
        num_min_second = 0

        for num in nums:
            if num_max == 0:
                num_max = num
            elif num > num_max:
                num_max_second = num_max
                num_max = num
            elif num_max_second == 0:
                num_max_second = num
            elif num > num_max_second:
                num_max_second = num

        for num in nums:
            if num_min == 0:
                num_min = num
            elif num < num_min:
                num_min_second = num_min
                num_min = num
            elif num_min_second == 0:
                num_min_second = num
            elif num < num_min_second:
                num_min_second = num
        
        return (num_max * num_max_second) - (num_min * num_min_second)

#Time: O(N) + O(N) => O(N)
#Space: O(1)