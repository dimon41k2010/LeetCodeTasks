class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positive = []
        negative = []
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)

        res = []
        for i in range(len(positive)):
            res.append(positive[i])
            res.append(negative[i])
        return res


# Time: O(N)
# Space: O(N)