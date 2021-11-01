class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count_dict = {}
        for i in range(len(nums)):
            if nums[i] not in count_dict.keys():
                count_dict[nums[i]] = 1
            else:
                count_dict[nums[i]] += 1
        # print(count_dict)

        max_degree = 0
        set_candidates = set()
        for key in count_dict.keys():
            max_degree = max(count_dict[key], max_degree)

        for key in count_dict.keys():
            if count_dict[key] == max_degree:
                set_candidates.add(key)
        # print(set_candidates)
        min_diff = 1000000
        rev_nums = nums[::-1]
        for candidate in set_candidates:
            begin = nums.index(candidate)
            end = len(nums) - 1 - rev_nums.index(candidate)
            # print(begin, end, candidate)
            min_diff = min(end - begin + 1, min_diff)
        return(min_diff)
        

    