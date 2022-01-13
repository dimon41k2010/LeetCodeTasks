class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = None
        for i in range(0, len(nums)):
                # print('2:',index)
            if nums[i] >= target:
                index = i
                break
        if index == None:
            index = len(nums)
        return index
    
    #Time: O(n)
    #Space: O(1)