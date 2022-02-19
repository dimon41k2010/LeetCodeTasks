class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        odd = {}
        even = {}
        
        def add_to_dict(num, dict):
            if num not in dict.keys():
                dict[num] = 1
            else:
                dict[num] += 1

        def find_max_key(dict):
            max_key = -1
            max_val = -1
            for key in dict.keys():
                if max_val < dict[key]:
                    max_val = dict[key]
                    max_key = key
            return max_key

        def solve(dict1, dict2):
            max_key1 = find_max_key(dict1)
            dict2.pop(max_key1, None)

            if len(dict2) == 0:
                return dict1[max_key1]

            max_key2 = find_max_key(dict2)
            return dict1[max_key1] + dict2[max_key2]

        for i in range(len(nums)):
            if i % 2 == 0:
                add_to_dict(nums[i], even)
            elif i % 2 != 0:
                add_to_dict(nums[i], odd)


        return (len(nums) - max(solve(odd.copy(), even.copy()) , solve(even.copy(), odd.copy()) ))