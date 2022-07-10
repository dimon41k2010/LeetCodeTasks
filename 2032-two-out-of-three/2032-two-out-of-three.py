class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

#         sets = [set(nums1), set(nums2), set(nums3)]

#         res = set()
#         for set_ in sets:
#             for val in set_:
#                 counter = len([1 for set_inner in sets if val in set_inner])
#                 if counter > 1:
#                     res.add(val)

#         return list(res)

    
#Time: O(nums1 + nums2 + nums3) = O(N)
#Space: O(nums1 + nums2 + nums3) = O(N)

        sets = [set(nums1), set(nums2), set(nums3)]

        def number_occurrence(sets, val):
            return len([1 for set_ in sets if val in set_])

        res = set()
        for set_ in sets:
            for val in set_:
                if number_occurrence(sets, val) > 1:
                    res.add(val)
        return list(res)
    
    