class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        distinct = len(set(nums))

        def add_to_dic(d, key):
            if key in d.keys():
                d[key] += 1
            else:
                d[key] = 1

        def remove_from_dic(d, key):
            d[key] -= 1
            if d[key] == 0:
                d.pop(key)

        d = {}
        left = right = 0
        res = 0

        while right < len(nums) or left < right:
            while len(d.keys()) != distinct and right < len(nums):
                add_to_dic(d, nums[right])
                right += 1
                # print(res, left, right, len(d.keys()))

            if len(d.keys()) == distinct:
                res += len(nums) - right+1
            remove_from_dic(d, nums[left])
            left += 1

        return (res)
    
# Time: O(N)
# Space: O(N)