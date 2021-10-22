class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first_max = None
        second_max = None
        third_max = None


        for num in nums:
            if first_max is None or first_max < num:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif second_max is None or second_max < num:
                third_max = second_max
                second_max = num
            elif third_max is None or third_max < num:
                third_max = num

        first_min = None
        second_min = None

        for num in nums:
            if first_min is None or first_min > num:
                second_min = first_min
                first_min = num
            elif second_min is None or second_min > num:
                second_min = num
        res = max(first_max * second_max * third_max, first_max * first_min * second_min)

        return (res)