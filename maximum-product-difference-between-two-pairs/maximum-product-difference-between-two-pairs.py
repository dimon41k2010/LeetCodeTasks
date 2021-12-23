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

# #Time: O(N) + O(N) => O(N)
# #Space: O(1)


# recursion
        def find_max(index, nums):
            if index > len(nums)-1:
                return 0,0

            n_max, n_max_second = find_max(index+1, nums)
            num = nums[index]

            if n_max == 0:
                n_max = num
            elif num > n_max:
                n_max_second = n_max
                n_max = num
            elif n_max_second == 0:
                n_max_second = num
            elif num > n_max_second:
                n_max_second = num

            return n_max, n_max_second

        n_max, n_max_second = find_max(0, nums)

        def find_min(index, nums):
            if index > len(nums)-1:
                return 0,0

            n_min, n_min_second = find_min(index+1, nums)
            num = nums[index]

            if n_min == 0:
                n_min = num
            elif num < n_min:
                n_min_second = n_min
                n_min = num
            elif n_min_second == 0:
                n_min_second = num
            elif num < n_min_second:
                n_min_second = num

            return n_min, n_min_second

        n_min, n_min_second = find_min(0, nums)

        return ( n_max * n_max_second) - (n_min * n_min_second)
    
#Time: O(N) + O(N) => O(N)
#Space: O(N) + O(N) => O(N)
