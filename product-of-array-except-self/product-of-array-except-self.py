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


# ==== second solution
        def solve_no_zero(nums):
            prod = 1
            res = []
            for num in nums:
                prod *= num
            for num in nums:
                res.append(prod // num)
            return res

        def solve_one_zero(nums):
            prod = 1
            for num in nums:
                if num == 0:
                    continue
                prod *= num

            res = []
            for num in nums:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res

        def solve_more_zero(nums):
            return [ 0 for _ in nums]

        
        count_zero = nums.count(0)
        if count_zero == 0:
            return (solve_no_zero(nums))
        elif count_zero == 1:
            return (solve_one_zero(nums))
        else:
            return (solve_more_zero(nums))

#Time: O(N)
#Space: O(N)
