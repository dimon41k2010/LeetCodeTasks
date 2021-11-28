class Solution:
    def check(self, nums: List[int]) -> bool:
        counter = 0
        for index in range(1, len(nums)):
            if nums[index-1] > nums[index]:
                if counter < 1 and nums[index] <= nums[0] and nums[0] >= nums[-1]:
                    counter += 1
                else:
                    return False

        return (True)

# Time: O(N)
# Space: O(1)