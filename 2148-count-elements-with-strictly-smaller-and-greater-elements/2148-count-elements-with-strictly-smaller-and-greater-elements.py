class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        res = 0
        min_ = 100000
        max_ = -100000
        for num in nums:
            if min_ > num:
                min_ = num
            if max_ < num:
                max_ = num

        for num in nums:
            if num != min_ and num != max_:
                res += 1
        return (res)

# Time: O(N) + O(N) = O(N)
# Space: O(1)

        # used = set([min(nums), max(nums)])
        # return (len([ num for num in nums if num not in used ]))

# Time: O(N) + O(N) = O(N)
# Space: O(N)
        