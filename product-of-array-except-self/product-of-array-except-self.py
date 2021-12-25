class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_prod = []
        suffix_prod = []
        sum_p = 1
        sum_s = 1
        left, right = 0, len(nums)-1
        while left < len(nums):
            sum_p *= nums[left]
            prefix_prod.append(sum_p)
            sum_s *= nums[right]
            suffix_prod.append(sum_s)
            left += 1
            right -= 1
        suffix_prod.reverse()

        res = []
        for i in range(len(nums)):
            prefix = 1
            suffix = 1
            if i-1 >= 0:
                prefix = prefix_prod[i-1]
            if i+1 < len(nums):
                suffix = suffix_prod[i+1]

            res.append(prefix * suffix)

        return(res)

#Time: O(N) + O(N) + O(N) => O(N)
#Space: O(N) + O(N) => O(N)