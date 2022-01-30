class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        ones = nums.count(1)
        zeros = 0
        res = []
        max_division_score = 0

        for i in range(len(nums)+1):
            division_score = ones + zeros
            if max_division_score < division_score:
                res = [i]
                max_division_score = division_score
            elif max_division_score == division_score:
                res.append(i)
            
            if i >= len(nums):
                continue
                
            if nums[i] == 1:
                ones -= 1
            if nums[i] == 0:
                zeros += 1

        return res


# Time: O(N)
# Space: O(1)