class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) / 2
        nums_set = set()
        
        for num in nums:
            if num in nums_set:
                return num
            nums_set.add(num)