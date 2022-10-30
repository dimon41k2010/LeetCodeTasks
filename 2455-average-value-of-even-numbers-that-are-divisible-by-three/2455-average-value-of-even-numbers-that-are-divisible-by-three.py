class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        sum_ = 0
        for num in nums:
            if num % 2==0 and num % 3==0:
                sum_ += num
                count += 1

        res = (sum_ // count) if count != 0 else 0
        return(res)