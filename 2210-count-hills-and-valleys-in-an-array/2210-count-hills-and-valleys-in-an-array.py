class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums)-1):
            if nums[i-1] == nums[i]:
                continue
            next = i+1
            while next < len(nums) and nums[i] == nums[next]:
                next += 1
            if next == len(nums):
                break
            if nums[i-1] < nums[i] and nums[i] > nums[next]:
                res += 1
            if nums[i-1] > nums[i] and nums[i] < nums[next]:
                res += 1

        return(res)

# Time: O(N)
# Space: O(1)
         