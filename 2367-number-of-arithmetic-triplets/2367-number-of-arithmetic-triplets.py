class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        set_num = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i]-diff in set_num and nums[i]+diff in set_num:
                res += 1
        return (res)

#Time: O(N)
#Space: O(N)
