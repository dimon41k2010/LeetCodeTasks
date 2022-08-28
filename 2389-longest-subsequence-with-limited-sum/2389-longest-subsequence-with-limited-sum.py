class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = []
        for query in queries:
            sub_sum = 0
            for nums_i in range(len(nums)):
                sub_sum += nums[nums_i]
                if query < sub_sum:
                    answer.append(nums_i)
                    break
                elif len(nums)-1 == nums_i:
                    answer.append(nums_i+1)
        return (answer)