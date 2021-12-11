class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        # print(max_candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return (res)