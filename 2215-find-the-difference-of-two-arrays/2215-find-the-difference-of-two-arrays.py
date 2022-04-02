class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        
        return [list(set_1 - set_2), list(set_2 - set_1)]
    
    
# Time: O(N)
# Space: O(N)