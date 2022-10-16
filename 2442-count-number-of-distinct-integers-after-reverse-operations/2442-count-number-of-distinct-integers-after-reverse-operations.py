class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        def int_flip(num):
            res = 0
            while num:
                res = res * 10 + num % 10
                num //= 10
            return res

        set_ = set(nums)
        for num in nums:
            set_.add(int_flip(num))
        return (len(set_))

#Time: O(N)
#Space: O(N)