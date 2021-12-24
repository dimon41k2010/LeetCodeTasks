class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_ = 0
        index = 0
        res = len(nums)+1
        for i in range(len(nums)):
            sum_ += nums[i]

            while index < i and sum_ >= target:
                res = min(res, i - index + 1)
                sum_ -= nums[index]
                index += 1

            if sum_ >= target:
                res = min(res, i - index + 1)
        
        if res == len(nums)+1:
            return 0
        
        return (res)
    
    
#Time: O(2 * N) => O(N)
#Space: O(1)