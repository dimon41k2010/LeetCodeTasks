class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
#         d = {}
#         s = set()

#         for num in nums:
#             if num in s and num+1 not in s:
#                 continue
#             print(num)
#             if num not in d.keys():
#                 d[num] = 1
#             else:
#                 d[num] += 1
#             s.add(num)
            
#             if num+1 in s:
#                 s.remove(num+1)
#         res = -1
#         for key in d.keys():
#             if key+1 in d.keys():
#                 low = d[key]
#                 high = d[key+1]
#                 temp_res = -1
#                 if low <= high:
#                     temp_res = low * 2
#                 elif low > high:
#                     temp_res = high * 2 + 1
#                 res = max(res, temp_res)
        # return res
    
# not correct answer

        n = len(nums)
        res = dp = -1
        for i in range(1, n):
            if dp > 0 and nums[i] == nums[i - 2]:
                dp += 1
            else:
                dp = 2 if nums[i] == nums[i - 1] + 1 else -1
            res = max(res, dp)
        return res
        