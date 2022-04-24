class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        sets = [set(num) for num in nums]
        res = []

        for num in nums[0]:
            if all([num in set_ for set_ in sets]):
                res.append(num)

        return (sorted(res))

# Time: O(N * L) // N = len(nums), L = len(nums[0])
# Space: O(N * L)


#======== Second method with count dict

#         count_dict = {}

#         for sub_nums in nums:
#             for num in sub_nums:
#                 if num not in count_dict.keys():
#                     count_dict[num] = 1
#                 else:
#                     count_dict[num] += 1
                    
#         return ([ key for key in range(1,1001) if key in count_dict.keys() and count_dict[key]==len(nums) ])

# Time: O(N * L) // N = len(nums), L = len(nums[0])
# Space: O(N * L)