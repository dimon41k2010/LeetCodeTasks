class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return (res)
    
# Time: O(N^2)
# Space: O(1)
        
    
    #Second solution with slicing
        r = []
        for val, idx in enumerate(index):
            r = r[:idx] + [nums[val]] + r[idx:]
            return(r)
        
        
# Time: O(N^2)
# Space: O(1)